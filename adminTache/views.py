from django.shortcuts import render
from django.http import HttpResponse 
from adminTache.models import Tache,Matiere
from adminTache.forms import *
from django.template import RequestContext, Template
from django.views import generic  
from django.utils import timezone
# Create your views here.
def index(request):
    formulaireRecherche=RechercheTacheForm()
    if request.method == 'POST':
        formulaireRecherche=RechercheTacheForm(request.POST)
        if formulaireRecherche.is_valid():
            seance=formulaireRecherche.cleaned_data['seance']
            return(matiere(request,seance.matiere.titre))
        else:
            formulaire='<form action="" method="post">{% csrf_token %}'+str(formulaireRecherche)+"<input type='submit' value='Rechercher'></form>"
            temp=Template(formulaire+"<br><a href='list'>Afficher la liste des tâches</a>")
            context =RequestContext(request)
            return HttpResponse(temp.render(context))  
    else:
        formulaire='<form action="" method="post">{% csrf_token %}'+str(formulaireRecherche)+"<input type='submit' value='Rechercher'></form>"
        temp=Template(formulaire+"<br><a href='list'>Afficher la liste des tâches</a>")
        context =RequestContext(request)
        return HttpResponse(temp.render(context))  
def list(request):
    retour=''
    for t in Tache.objects.all():
        retour+=str(t)+'<br>_________________<br>'
    retour=retour.replace('\n','<br>')
    retour=retour.replace('\t','&emsp;')
    return HttpResponse(retour)
def tache(request,tache_id):
    try:
        retour=str(Tache.objects.get(id=tache_id))
        retour=retour.replace('\n','<br>')
        retour=retour.replace('\t','&emsp;')
        return HttpResponse(retour)
    except Exception:
        return(list(request))
def matiere(request,matiere_titre):
    try:
        retour=''
        for t in Tache.objects.filter(seance__matiere__titre=matiere_titre):
            retour+=str(t)+'<br>_________________<br>'
        retour=retour.replace('\n','<br>')
        retour=retour.replace('\t','&emsp;')
        return HttpResponse(retour)
    except Exception as e :
        return HttpResponse(e)
    
def toDoList(request,tache_a_faire):
    try:
        retour=''
        for t in Tache.objects.filter(faite=tache_a_faire):
            retour+=str(t)+'<br>_________________<br>'
        retour=retour.replace('\n','<br>')
        retour=retour.replace('\t','&emsp;')
        return HttpResponse(retour)
    except Exception as e :
        return HttpResponse(e)
        
class tacheListDetailView(generic.list.ListView):
    model=Tache
    template_name='tache_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for object in self.object_list:
            if object.faite == True :
                object.faite='Faite'
            else:
                object.faite='En cours'
        return context

class tacheDetailView(generic.detail.DetailView):
    model=Tache
    template_name='tache_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.faite == True :
            self.object.faite='Faite'
        else:
            self.object.faite='En cours'
        context['now']=timezone.now()
        return context
