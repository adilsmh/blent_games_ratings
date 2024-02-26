import psycopg2
import pandas as pd
from tqdm import tqdm

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime
from dateutil.relativedelta import relativedelta
from pymongo import MongoClient


def create_table(conn_engine, cursor, table_name="games_ratings"):
    # Define table schema #
    cur = cursor

    # Define table schema
    create_schema_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        game_id VARCHAR PRIMARY KEY,
        average_rating FLOAT,
        user_rating_count INTEGER NOT NULL,
        recent_rating INTEGER,
        oldest_rating INTEGER
    );
    """
    print("Create table if not already exists")
    cur.execute(create_schema_query)

    # Commit sql query instructions
    conn_engine.commit()


def mongodb_data_fetcher(host, username, password, time_window_months=120):
    # Define MongoDB Atlas login credentials and URI
    username = "admin"
    password = "iFcQrztMFU5SLqrS"
    host = "34.244.254.17:27017"

    mongodb_URI = f"mongodb://{username}:{password}@{host}/?directConnection=true"

    # Connection to the database with error handling
    client = MongoClient(mongodb_URI)
    print("Connection established")

    # Retrieve games ratings document collection from the database
    db = client["videoGamesDB"]
    collection = db["games_ratings"]

    # Define list to collect fetched documents
    rows_l = []

    # Define threshold given number of months declared
    window_threshold = (
        datetime.today() - relativedelta(months=time_window_months)
    ).strftime("%Y-%m-%d")

    for doc in collection.aggregate(
        [
            # Adding new converted ISO date column from unixdatetime existing column
            {
                "$addFields": {
                    "reviewDate": {
                        "$dateToString": {
                            "format": "%Y-%m-%d",
                            "date": {
                                "$toDate": {"$multiply": ["$unixReviewTime", 1000]}
                            },
                        }
                    },
                }
            },
            # Matching only legit reviews and only most recent ones given the time threshold
            {"$match": {"verified": True, "reviewDate": {"$gte": window_threshold}}},
            {"$sort": {"reviewdate": -1}},  # sort reviews by most recent reviews
            # Group data by unique game and add new info column
            {
                "$group": {
                    "_id": "$asin",
                    "average_rating": {"$avg": "$overall"},
                    "user_rating_count": {"$count": {}},
                    "recent_rating": {"$first": "$overall"},
                    "oldest_rating": {"$last": "$overall"},
                },
            },
            {
                "$sort": {"average_rating": -1}
            },  # sort game review by rating from the highest to the lowest
            {"$limit": 15},  # retrieve only the first 15 highest rated games
        ],
    ):
        rows_l.append(doc)  # append document to the list

    # Define new dataframe collecting all the fetched data from mongodb
    ratings_df = (
        pd.DataFrame(rows_l).rename(columns={"_id": "game_id"}).round(decimals=2)
    )

    return ratings_df


def postgres_data_injector():
    # Declare identification credentials to connect into RDS Postresql DB Instance
    print("Connection to the DB Instance")
    conn = psycopg2.connect(
        host="3.252.135.5",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="ikRCGzzAYLLG",
    )
    print("Connection established")

    # Define cursor to move into the server
    cursor = conn.cursor()

    # Create table schema if not already exists
    create_table(conn_engine=conn, cursor=cursor)

    # Fetch data from mongoDB collection
    data = mongodb_data_fetcher()

    # Injecting data into Postregres DB Instance
    data = mongodb_data_fetcher()
    print("Injecting data to the database")

    # Define sql query instruction dealying with game review duplicates and updating with new data if conflict
    sql_inj_query = """
    INSERT INTO games_ratings(game_id, average_rating, user_rating_count, recent_rating, oldest_rating)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (game_id) DO UPDATE
    SET
    average_rating = EXCLUDED.average_rating,
    user_rating_count = EXCLUDED.user_rating_count,
    recent_rating = EXCLUDED.recent_rating,
    oldest_rating = EXCLUDED.oldest_rating;
    """

    for _, row in tqdm(data.iterrows()):
        cursor.execute(
            sql_inj_query,
            (
                row.game_id,
                row.average_rating,
                row.user_rating_count,
                row.recent_rating,
                row.oldest_rating,
            ),
        )
    print("Injectiion successfull")

    # Commit injection query instructions
    conn.commit()

    # Close cursor and connection
    cursor.close()
    conn.close()

# Define the Airflow DAG (Directed Acyclic Graph)
dag = DAG(
    "Pipeline pour recccolte de données de jeux videos",
    description="Pipeline d'avis jeux videos",
    schedule_interval="@daily",
    start_date=datetime.utcnow(),
)

# Define the tasks in the DAG
extract_transform = PythonOperator(
    task_id="extract_and_transform", python_callable=mongodb_data_fetcher, dag=dag
)

load = PythonOperator(
    task_id="load_to_db", python_callable=postgres_data_injector, dag=dag
)

# Set task dependencies
extract_transform >> load
