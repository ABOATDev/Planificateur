from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse 
from app.models import Tache,Personne,Projet
# from app.forms import *
from django.template import RequestContext, Template
from django.views import generic  
from django.utils import timezone

# Create your views here.
def index(request):
    temp=Template(
    "<br><a href='tache'>Afficher la liste des tâches</a>"
    +"<br><a href='personne'>Afficher la liste des personnes</a>"
    +"<br><a href='projet'>Afficher la liste des projets</a>")
    context =RequestContext(request)
    return HttpResponse(temp.render(context))  

# Tache
class tacheListDetailView(generic.list.ListView):
    model=Tache
    template_name='tache_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class tacheDetailView(generic.detail.DetailView):
    model=Tache
    template_name='tache_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now']=timezone.now()
        return context

class tacheByProjetListDetailView(generic.list.ListView):
    # get all taches by projet
    model=Tache
    template_name='tacheByProjet_list.html'
    
    def get_queryset(self):
        return Tache.objects.filter(projet=self.kwargs['pk'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projet'] = Projet.objects.get(pk=self.kwargs['pk'])

        return context

# Personne
class personneListDetailView(generic.list.ListView):
    model=Personne
    template_name='personne_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class personneDetailView(generic.detail.DetailView):
    model=Personne
    template_name='personne_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Projet
class projetListDetailView(generic.list.ListView):
    model=Projet
    template_name='projet_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class projetDetailView(generic.detail.DetailView):
    model=Projet
    template_name='projet_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now']=timezone.now()
        return context
