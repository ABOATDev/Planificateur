from django.db import models
from datetime import timezone,timedelta,datetime
# L'objectif est de décrire les entités nécessaire à la gestion de tâches dans le cadre des projets réalisés durant les formations IPI

class Intervenant(models.Model):    
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
   
    def __str__(self):
        return(self.nom+' '+self.prenom)

class Matiere(models.Model):    
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    intervenant = models.ForeignKey(Intervenant, on_delete=models.CASCADE)    
    description = models.CharField(max_length=200)
    titre = models.CharField(max_length=7,default='IPYT011')

    def __str__(self):
        return(self.titre+'\t\t: '+self.description+'\nIntervenant\t\t: '+str(self.intervenant))

class Seance(models.Model):    
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    date_heure_debut = models.DateField(default=datetime.now(timezone(timedelta(0))))
    duree = models.IntegerField(default=1) # représente le nombre d'heure à réaliser pour la tâche identifiée
    
    def __str__(self):
        return(self.matiere.titre+'\t\t\t: '+str(self.date_heure_debut)+'\nNombre d\'heures\t\t: '+str(self.duree)+'h')
   
# Une tâche est identifiée par un ID autoincrémenté et consiste en une durée (en heure) et une description (max 200 car) 
# On associera une tâche à une matière par le biais d'une clé étrangère 
class Tache(models.Model):
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)    
    duree = models.IntegerField(default=1) # représente le nombre d'heure à réaliser pour la tâche identifiée
    description = models.CharField(max_length=200)
    titre = models.CharField(max_length=50,default='Faire une pause')
    faite = models.BooleanField(default=False)
    
    def __str__(self):
        return(self.titre+'\t\t: '+'En cours'*(not self.faite)+'Faite'*(self.faite)+'\nDescription\t\t: '+self.description+'\nNombre d\'heures\t\t: '+str(self.duree)+'h\n'+str(self.seance))
