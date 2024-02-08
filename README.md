Amélioration du Catalogue de Vente en Ligne pour une Enseigne de Jeux Vidéos
============================================================================

Description du Projet
---------------------

Une enseigne de jeux vidéos cherche à améliorer son catalogue de vente en ligne en proposant une liste des jeux les mieux notés et les plus appréciés de la communauté sur les derniers jours. Pour cela, elle souhaite récupérer les avis les plus récents de ses propres clients en ligne pour déterminer les jeux les mieux notés. Les développeurs Web de l'entreprise souhaitent pouvoir requêter ces informations sur une base de données SQL qui va historiser au jour le jour les jeux les mieux notés.

Les données brutes sont stockées dans une base MongoDB, et il est supposé que celles-ci sont ajoutées au fur et à mesure par d'autres programmes (API backend). L'objectif est de construire un pipeline de données qui va alimenter automatiquement un Data Warehouse (représenté par une base de données SQL) tous les jours en utilisant les données depuis la base MongoDB. Ce pipeline de données doit être développé en Python.

### Contraintes

-   Les informations des jeux les mieux notés doivent être exactes et faciles à manipuler.
-   Le Data Warehouse doit être une base de données compatible SQL : MySQL, PostgreSQL ou MariaDB.
-   Le pipeline doit éviter les doublons et ne pas prendre en compte les avis de plus de 6 mois d'antériorité.
-   Chaque jour, les 15 jeux les mieux notés sur les 6 derniers mois seront ajoutés dans le Data Warehouse.

Description des Données
-----------------------

Les données sont disponibles sous forme de fichier compressé au format JSON. Chaque observation contient les caractéristiques suivantes :

-   reviewerID : identifiant unique de l'utilisateur.
-   verified : indique si l'utilisateur est un utilisateur vérifié (et non un robot).
-   asin : identifiant unique du produit.
-   reviewerName : nom/pseudo de l'utilisateur.
-   vote : nombre de votes associés à l'avis de l'utilisateur.
-   style : style associé au jeu vidéo.
-   reviewText : description complète de l'avis.
-   overall : note attribuée par l'utilisateur au jeu vidéo.
-   summary : résumé de l'avis.
-   unixReviewTime : timestamp de l'avis.
-   reviewTime : date de l'avis.
-   image : URL des images jointes par l'utilisateur.

Étapes du Projet
----------------

Afin de terminer le projet, toutes les étapes doivent être complétées.

1.  Ajouter les données brutes dans une base MongoDB
    -   Les données brutes seront ajoutées dans une collection de la base MongoDB.
2.  Créer la base de données SQL avec le schéma associé
    -   Une table avec un schéma associé doit être créée pour historiser les jeux les mieux notés.
3.  Développer le script Python du pipeline ETL
    -   Le pipeline consiste en un script Python qui va effectuer plusieurs opérations, y compris la récupération des avis des 6 derniers mois, l'agrégation des notes et des avis pour chaque jeu vidéo, et l'insertion des résultats dans la base SQL.
4.  Automatiser le pipeline avec un outil de planification
    -   Le script Python doit être adapté pour être utilisable par un outil de planification. On vérifiera que le workflow fonctionne correctement en l'exécutant sur des périodes antérieures différentes.
