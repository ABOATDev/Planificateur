from django.forms import ModelForm
from adminTache.models import *
class RechercheTacheForm(ModelForm):
    class Meta:
        model = Tache
        fields = ['seance']
        