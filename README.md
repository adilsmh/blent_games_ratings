Amélioration du catalogue de vente en ligne pour une enseigne de jeux vidéos
============================================================================

<b1>Diagramme ETL</b1>

![Diagramme ETL](https://github.com/adilsmh/blent_games_ratings/assets/76161036/a0285138-0d78-4d22-bb87-9c52acf5055a)

1\. Description du Projet
---------------------

Une enseigne de jeux vidéos cherche à améliorer son catalogue de vente en ligne en proposant une liste des jeux les mieux notés et les plus appréciés de la communauté sur les derniers jours. Pour cela, elle souhaite récupérer les avis les plus récents de ses propres clients en ligne pour déterminer les jeux les mieux notés. Les développeurs Web de l'entreprise souhaitent pouvoir requêter ces informations sur une base de données SQL qui va historiser au jour le jour les jeux les mieux notés.

Les données brutes sont stockées dans une base MongoDB, et il est supposé que celles-ci sont ajoutées au fur et à mesure par d'autres programmes (API backend). L'objectif est de construire un pipeline de données qui va alimenter automatiquement un Data Warehouse (représenté par une base de données SQL) tous les jours en utilisant les données depuis la base MongoDB. Ce pipeline de données doit être développé en Python.

2\. Objectifs du Projet
-----------------------

-   Améliorer le catalogue de vente en ligne en mettant en avant les jeux les mieux notés et les plus appréciés par la communauté.
-   Proposer une liste des jeux les mieux notés pour la page d'accueil du site et les campagnes de communication.
-   Automatiser le processus d'ETL pour mettre à jour régulièrement les données dans le Data Warehouse.

3\. Méthodologie
----------------

### 3.1. Compréhension du Problème

-   Objectifs : Amélioration du catalogue de vente en ligne en mettant en avant les jeux les mieux notés.
-   Sources de Données : Avis des clients en ligne stockés dans une base MongoDB.
-   Contraintes :
    -   Les informations des jeux les mieux notés doivent être exactes et faciles à manipuler.
    -   Le Data Warehouse doit être une base de données compatible SQL :
        -   MySQL
        -   PostgreSQL
        -   MariaDB
    -   Le pipeline doit éviter les doublons et ne pas prendre en compte les avis de plus de 6 mois d'antériorité.
    -   Chaque jour, les 15 jeux les mieux notés sur les 6 derniers mois seront ajoutés dans le Data Warehouse.

### 3.2. Compréhension des Données

- Les données sont disponible sous forme de fichier compressé au format JSON. Chaque observation contient les caractéristiques suivantes:
    - reviewerID : identifiant unique de l'utilisateur.
    - verified : indique si l'utilisateur est un utilisateur vérifié (et non un robot).
    - asin : identifiant unique du produit.
    - reviewerName : nom/pseudo de l'utilisateur.
    - vote : nombre de votes associés à l'avis de l'utilisateur.
    - style : style associé au jeu vidéo.
    - reviewText : description complète de l'avis.
    - overall : note attribuée par l'utilisateur au jeu vidéo.
    - summary : résumé de l'avis.
    - unixReviewTime : timestamp de l'avis.
    - reviewTime : date de l'avis.
    - image : URL des images jointes par l'utilisateur.

### 3.3. Préparation des Données

-   Conception de la pipeline ETL pour extraire, transformer et charger les données.

### 3.4. Modélisation de la base de données

-   Création du schéma de la base de données SQL pour stocker les données préparées.

4\. Guide d'Utilisation
-----------------------

Ce projet comprend un script Python pour les différentes étapes du processus ETL. Voici le guide d'utilisation :

-   `pipeline.py` :
    - Ce script se port de main et contient toutes les functions suivantes :
        - create_table() : Définit le schéma de la table à creer si elle n'existe déjà.
        - data_fetcher() : Extrait les données depuis la base de données MongoDB et effectue toutes les agrégations et transformations requises.
        - data_injector() : Realise l'injection des nouvelles données récupérées dans la base de données (Data Warehouse) PosgreSQL, en prenant les précautions nécessaires (remplacement des doublons).

5\. Outils et Technologies
--------------------------

Ce projet utilise les outils et technologies suivants :

-   Python : Langage de programmation principal pour le développement des scripts.
-   MongoDB : Base de données NoSQL pour stocker les données brutes.
-   PostgreSQL : Base de données relationnelle pour le Data Warehouse.
-   PyMongo : Pilote Python pour interagir avec MongoDB.
-   Psycopg2 : Pilote Python pour interagir avec PostgreSQL.

6\. Installation et Configuration
---------------------------------

Pour exécuter ce projet, assurez-vous d'avoir les prérequis suivants installés :

-   Python 3.8.8 ou une version supérieure
-   MongoDB
-   PostgreSQL

Assurez-vous également d'installer les dépendances Python nécessaires en exécutant `pip install -r requirements.txt`.
