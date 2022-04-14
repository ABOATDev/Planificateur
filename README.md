# Mini-projet de Python-Django : Planificateur  - IPYT011
Création d'un planificateur de tâche, en django.

Projet de l'école informatique IPI BAC+3 [CDA (Concepteur Développeur d’Applications)](https://www.ipi-ecoles.com/concepteur-developpeur-applications/).

Temps passé sur le projet : 6 heures

## Avant-propos et conseils de réalisation
L'objectif est de réaliser une application Web qui réponde à un besoin identifier dans le cahier des charges. 
Le travail est à réaliser durant les séances de IPYT011 prévues à cet effet.
Le travail est à réaliser en groupe et déposer dans la boîte prévue à cet effet le mardi 12 avril 2022 à 16h30.
Veillez à bien réaliser votre projet en suivant une méthode de développement qui permettent d'analyser le cahier des charger, de concevoir l'application, de l'implémenter sous Django et de la tester. 
Pensez à prendre des notes et à rédiger votre rapport de réalisation et votre présentation au fur et à mesure du développement.


## Cahier des charges

### Contexte métier
Une entreprise a besoin d'une application permettant au personnel de suivre un tableau de tâches à réaliser dans le cadre d'un projet. L'objectif est que l'application soit capable de proposer une organisation de tâches la plus efficace en fonction de plusieurs facteurs qui permettront de les prioriser, répartir entre les membres des équipes de développement et les ordonnancer dans le temps.
Un processus de validation des tâches au fur et à mesure de leur statut (planifiée, en cours, réalisée, en pause, validée) permettra aux différent·es responsables d'évaluer l'état d'avancement du projet au regard d'une date de livraison imposée.
Ces responsables de projet auront la possibilité d'avancer ou de reculer la date de livraison et choisissant d'éliminer ou d'ajouter des tâches ou en réduisant ou augmentant le temps de réalisation planifié.
Les responsables sont également chargés de valider une tâche une fois celle-ci réalisée. 
Les personnes en charge de tâches doivent faire à rapport quotidien de l'état d'avancement d'une tâche en remplissant un formulaire. Une ou plusieurs personnes peuvent être en charge de la réalisation mais une seule est chargée du rapport sur l'état d'avancement mesuré en pourcentage.
Les personnels, exécutant les tâches ou responsables, peuvent 
•	prendre des congés,
•	tomber malades,
•	arriver en cours de projet,
•	partir en cours de projet,
•	changer de tâches en cours de réalisation.
 
### Tâches
Une tâche est associée à un projet, à une ou plusieurs personnes exécutant·es dont une chargée de l'état d'avancement. 
Elle dispose d'une description, d'une priorité (sur 3 niveaux), d'une date de démarrage, d'une durée en jours, d'un statut, d'un état d'avancement.  
Elle peut aussi être associée à une ou plusieurs tâches précédentes nécessaires à sa réalisation.
Toutes les tâches dont les informations nécessaires à sa planification sont manquantes sont par défaut en pause.
Chaque tâche peut-être également associée à des sous-tâches qui la compose et/ou à une et une seule super-tâche dont elle est composante.

### Projets
Un projet est associé à plusieurs tâches qui sont nécessaire à sa réalisation ainsi qu'à un·e responsable.
Il dispose d'une date de livraison, qui est fixée par le ou la responsable et d'une date de démarrage, qui correspond à celle de la première tâche planifiée.
Il dispose également d'un statut (en pause, planifié, en cours, livré). Un projet dont l'ensemble des tâches n'ont pas été planifiés est en pause, un projet en cours a été planifié et la date de démarrage de la première tâche planifiée a été passée. Un projet dont l'ensemble des tâches est en pause est en pause également. Un projet est livré si l'ensemble des tâches ont été validées et réalisées.
Il dispose enfin d'un état d'avancement en pourcentage dont le calcul sera laissé à appréciation.

___

## Lancer le projet 


Pour commencer, initialisé la base de données :

```bash
python manage.py makemigrations
python manage.py migrate
```

Pour lancer le projet :

```bash
python manage.py runserver
```

Le projet se lance sur http://127.0.0.1:8000/ 



## Espace administration : 


L'espace admin web de django se trouve sur http://127.0.0.1:8000/admin/ en saisissant l'identifiant super admin ci-dessous.


### Identifiant : 
Login : dev

Mot de passe : azerty  





