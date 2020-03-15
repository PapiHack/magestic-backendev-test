# Test technique dev backend (Magestic)  

Petite application développée en `Django` pour les besoins de ce test technique.
Elle permet d'effectuer des opérations de type `CRUD` (Create, Read, Update and Delete) sur des entités `Employe` dont les propriétés sont : `nom`, `prénom`, `date de naissance` `fonction`, `photo de profil`.  

## Stack Technique  

- Django  
- Bootstrap 4  
- SQLite 3

## Installation  

- Installer les dépendances lister au niveau du fichier `requirements.txt` => `pip install -r requirements.txt`  

- Installer les migrations => `python manage.py makemigrations`  

- Appliquer les migrations => `python manage.py migrate`

- Démarer le serveur => `python manage.py runserver`  

### Notes  

Veillez à ce que `Python` soit disponible en ligne de commande et placez-vous au niveau du répertoire `magestic_test` avant d'exécuter les commandes ci-dessus.  
