from django.db import models
from datetime import timezone,timedelta,datetime
# L'objectif est de décrire les entités nécessaire à la gestion de tâches dans le cadre des projets réalisés durant les formations IPI

class Personne(models.Model):    
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    CONGE = 'CONGE'
    MALADE = 'EST MALADE'
    VIENSDARRIVE = 'VIENS DARRIVER'
    ABSENT  = "ABSENT"
    NORMAL  = "NORMAL"
    
    STATUT_CHOICES = (
        (CONGE, 'FINI'),
        (MALADE,  'EST MALADE'),
        (VIENSDARRIVE, 'VIENS DARRIVER'),
        (NORMAL, 'NORMAL'),
        (ABSENT, 'ABSENT')
    )

    # Le statut de la personne est défini par un choix dans la liste STATUT_CHOICES
    statut = models.CharField(
        max_length=2,
        choices=STATUT_CHOICES,
        default=NORMAL,
    )
    def __str__(self):
        return(self.nom+' '+self.prenom)

  
# Une tâche est identifiée par un ID autoincrémenté et consiste en une durée (en heure) et une description (max 200 car) 
# On associera une tâche à une matière par le biais d'une clé étrangère 
class Tache(models.Model):
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée
    libelle = models.CharField(max_length=200)

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
    status = models.CharField(
        max_length=2,
        choices=STATUT_CHOICES,
        default=ACOMMENCER,
    )

    # L'etat de l'avancement de la tache est définie par un nombre entier
    etat_avancement = models.IntegerField(default=1)
    
    def __str__(self):
        return(self.description+'\nPriorité\t\t\t: '+str(self.priorite)+'\nDate de début\t\t: '+str(self.date_debut)+'\nStatut\t\t\t: '+str(self.statut)+'\nEtat d\'avancement\t: '+str(self.etat_avancement))


class Projet(models.Model):    
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée

    #description VARCHAR(250),
    libelle = models.CharField(max_length=250, default="Tache sans nom")

    #date_livraison DATE NOT NULL,
    date_livraison = models.DateField(null=False)

    FINI = 'FINI'
    ENCOURS = 'EN COURS'
    ACOMMENCER = 'A COMMENCER'
    STATUT_CHOICES = (
        (FINI, 'FINI'),
        (ENCOURS, 'EN COURS'),
        (ACOMMENCER, 'A COMMENCER')
    )

    # Le statut de la tache est défini par un choix dans la liste STATUT_CHOICES
    status = models.CharField(
        max_length=2,
        choices=STATUT_CHOICES,
        default=ACOMMENCER,
    )

    #etat_avancement INT NOT NULL 1 to 100,
    etat_avancement = models.IntegerField(null=False, default=1)

    
    #date_debut DATETIME NOT NULL,
    date_debut = models.DateTimeField(null=False,default=datetime.now(timezone(timedelta(0))))

    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)    
    responsable = models.ForeignKey(Personne, on_delete=models.CASCADE)    

    def __str__(self):
        return(self.libelle+'\nDate de livraison\t: '+str(self.date_livraison)+'\nStatut\t\t\t: '+str(self.statut)+'\nEtat d\'avancement\t: '+str(self.etat_avancement))
