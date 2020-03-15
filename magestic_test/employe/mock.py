from .models import Employe
import os

def create_some_employees():
    """
    Je définis ici un espece de mock afin de peupler ma BD.
    """
    fake_infos = {
        'nom': 'Nom', 
        'prenom': 'Prenom', 
        'ddn': '1990-01-01', 
        'fonction': 'Fonction', 
    }
    i = 1
    while i <= 10:
        employe = Employe()
        employe.nom = fake_infos['nom'] + '--' + str(i)
        employe.prenom = fake_infos['prenom'] + '--' + str(i)
        employe.date_de_naissance = fake_infos['ddn']
        employe.fonction = fake_infos['fonction'] + '--' + str(i)
        employe.photo_de_profil = 'uploads/python.png'
        employe.save()
        i += 1