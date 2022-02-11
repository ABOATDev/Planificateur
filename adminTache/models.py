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
    description = models.CharField(max_length=200)

    # La priorité de la tache est définie par un nombre entre 1 et 5
    priorite = models.IntegerField(default=1)

    # La date de début de la tache
    date_debut = models.DateField(default=datetime.now(timezone(timedelta(0))))

    FINI = 'FINI'
    ENCOURS = 'EN COURS'
    ACOMMENCER = 'A COMMENCER'
    STATUT_CHOICES = (
        (FINI, 'FINI'),
        (ENCOURS, 'EN COURS'),
        (ACOMMENCER, 'A COMMENCER')
    )

    # Le statut de la tache est défini par un choix dans la liste STATUT_CHOICES
    statut = models.CharField(
        max_length=2,
        choices=STATUT_CHOICES,
        default=ACOMMENCER,
    )

    # L'etat de l'avancement de la tache est définie par un nombre entier
    etat_avancement = models.IntegerField(default=1)
    
    def __str__(self):
        return(self.description+'\nPriorité\t\t\t: '+str(self.priorite)+'\nDate de début\t\t: '+str(self.date_debut)+'\nStatut\t\t\t: '+str(self.statut)+'\nEtat d\'avancement\t: '+str(self.etat_avancement))
