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
    formulaire='<form action="" method="post"><input type="submit" value="Rechercher"></form>'
    temp=Template(formulaire+"<br><a href='list'>Afficher la liste des tâches</a>")
    context =RequestContext(request)
    return HttpResponse(temp.render(context))  

# Create your views here.
class tacheListDetailView(generic.list.ListView):
    model=Tache
    template_name='tache_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for object in self.object_list:
            object.faite = object.status
        return context
