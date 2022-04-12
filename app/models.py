from django.db import models

# Create your models here.
from django.db import models
from datetime import timezone,timedelta,datetime


class Personne(models.Model):    
    #clé primaire de l'entité autoincrémentée
    id = models.BigAutoField(primary_key=True) 
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)


    # L'objectif est de décrire les entités nécessaire à la gestion de tâches dans le cadre des projets réalisés durant les formations IPI
    CONGE = 'CONGE'
    MALADE = 'EST MALADE'
    VIENSDARRIVE = 'VIENS DARRIVER'
    ABSENT  = "ABSENT"
    NORMAL  = "NORMAL"

    STATUS_CHOICES = (
        (CONGE, 'FINI'),
        (MALADE,  'EST MALADE'),
        (VIENSDARRIVE, 'VIENS DARRIVER'),
        (NORMAL, 'NORMAL'),
        (ABSENT, 'ABSENT')
    )
    # Le statut de la personne est défini par un choix dans la liste STATUT_CHOICES
    statut = models.CharField(
        choices=STATUS_CHOICES,
        default=NORMAL,
        max_length=200
    )


    # Liste de tache de la personne
    taches = models.ManyToManyField('Tache',null=True,blank=True)


    def __str__(self):
        return(self.nom+' '+self.prenom)


class Projet(models.Model):    
    id = models.BigAutoField(primary_key=True) #clé primaire de l'entité autoincrémentée

    #description VARCHAR(250),
    libelle = models.CharField(max_length=250, default="Projet sans nom")

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
        choices=STATUT_CHOICES,
        default=ACOMMENCER,
        max_length=200
    )

    #etat_avancement pourcentage 1 to 100,
    etat_avancement = models.IntegerField(null=False, default=1)

    
    # Date de debut de la tache, par default la date de la création de la tache
    date_debut = models.DateTimeField(auto_now_add=True)
    #default=datetime.now(timezone(timedelta(0)))

    # Responsable du projet null 
    responsable = models.ForeignKey(Personne,null=True,blank=True, on_delete=models.SET_NULL)   

    def __str__(self):
        return(self.libelle+'\nDate de livraison\t: '+str(self.date_livraison)+'\nstatus\t\t\t: '+str(self.status)+'\nEtat d\'avancement\t: '+str(self.etat_avancement))


# Une tâche est identifiée par un ID autoincrémenté et consiste en une durée (en heure) et une description (max 200 car) 
# On associera une tâche à une matière par le biais d'une clé étrangère 
class Tache(models.Model):
    # Clé primaire de l'entité autoincrémentée
    id = models.BigAutoField(primary_key=True) 

    #La tache est relié à un projet
    projet = models.ForeignKey(Projet, on_delete=models.SET_NULL, null=True)


    #La tache est relié à un évaluateur
    evaluateur = models.ForeignKey(Personne, on_delete=models.SET_NULL, null=True)

    # La tache peut avoir 0 ou UNE tache parente
    tacheParente = models.ForeignKey('Tache', on_delete=models.SET_NULL, null=True, blank=True)


    # # Une liste de tache qui peut avoir 0 a plusieur tache
    # tacheDependance = models.ManyToManyField('Tache', through='TachePersonne',null=True,blank=True)


    # Nom de la tache
    libelle = models.CharField(max_length=200,default="Tache sans nom")

    description = models.CharField(max_length=200,default="Tache sans description")

    # La priorité de la tache est définie par un nombre entre 1 et 3
    priorite = models.IntegerField(default=1)

    # La date de début de la tache
    date_debut = models.DateField(auto_now_add=True)

    FINI = 'FINI'
    ENCOURS = 'EN COURS'
    ACOMMENCER = 'A COMMENCER'
    status_CHOICES = (
        (FINI, 'FINI'),
        (ENCOURS, 'EN COURS'),
        (ACOMMENCER, 'A COMMENCER')
    )

    # Le status de la tache est défini par un choix dans la liste status_CHOICES
    status = models.CharField(
        choices=status_CHOICES,
        default=ACOMMENCER,
        max_length=200
    )

    # L'etat de l'avancement de la tache est définie par un nombre entre 1 et 3
    etat_avancement = models.IntegerField(default=1)
    

    def __str__(self):
        return(self.description+'\nPriorité\t\t\t: '+str(self.priorite)+'\nDate de début\t\t: '+str(self.date_debut)+'\nstatus\t\t\t: '+str(self.status)+'\nEtat d\'avancement\t: '+str(self.etat_avancement))


