from django.db import models

# Create your models here.

class Employe(models.Model):
    """ 
    Définition du model Employé.
    """
    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    date_de_naissance = models.DateField(verbose_name='Date de naissance', null=False, blank=False)
    fonction = models.CharField(max_length=100, blank=False, null=False)
    photo_de_profil = models.ImageField(upload_to='uploads/', verbose_name='Photo de profil', null=False, blank=False)

    def __str__(self):
        return "Employe - {} {}".format(self.prenom, self.nom)
