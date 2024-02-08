Amélioration du catalogue de vente en ligne pour une enseigne de jeux vidéos
============================================================================

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
-   Contraintes
    -   Les informations des jeux les mieux notés doivent être exactes et faciles à manipuler.
    -   Le Data Warehouse doit être une base de données compatible SQL : MySQL, PostgreSQL ou MariaDB.
    -   Le pipeline doit éviter les doublons et ne pas prendre en compte les avis de plus de 6 mois d'antériorité.
    -   Chaque jour, les 15 jeux les mieux notés sur les 6 derniers mois seront ajoutés dans le Data Warehouse.

### 3.2. Compréhension des Données

-   Collecte des données brutes depuis la base MongoDB.
-   Exploration des données pour comprendre leur structure et leur qualité.

### 3.3. Préparation des Données

-   Nettoyage des données en éliminant les valeurs manquantes et les duplicatas.
-   Transformation des données pour agréger les avis par jeu vidéo.

### 3.4. Modélisation des Données

-   Création du schéma de la base de données SQL pour stocker les données préparées.
-   Conception des pipelines ETL pour extraire, transformer et charger les données.

### 3.5. Évaluation

-   Évaluation de la qualité des données transformées.
-   Vérification que les données chargées dans le Data Warehouse répondent aux exigences métier.

### 3.6. Déploiement

-   Déploiement des pipelines ETL dans un environnement de production.
-   Automatisation des tâches de traitement des données avec Cron.

### 3.7. Suivi et Maintenance

-   Surveillance des performances des pipelines ETL et du Data Warehouse.
-   Mise à jour des pipelines et du schéma de la base de données en fonction des évolutions des besoins métier.

4\. Guide d'Utilisation
-----------------------

Ce projet comprend plusieurs scripts Python pour les différentes étapes du processus ETL. Voici un guide d'utilisation pour chaque script :

-   `import_data.py` : Ajoute les données brutes dans la base MongoDB.
-   `etl_pipeline.py` : Effectue l'extraction, la transformation et le chargement des données dans le Data Warehouse.
-   `load_data.py` : Charge les résultats dans la base de données SQL.

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
