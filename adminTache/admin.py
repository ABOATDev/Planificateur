from django.contrib import admin
from adminTache.models import *
# modification des champs accessibles à l'administration

class IntervenantAdmin(admin.ModelAdmin):
    search_fields=['nom','prenom']
class MatiereAdmin(admin.ModelAdmin):
    fields=['titre','intervenant','description']
    search_fields=['titre','intervenant__nom','intervenant__prenom']
# Register your models here.
admin.site.register(Intervenant,IntervenantAdmin)
admin.site.register(Matiere,MatiereAdmin)
admin.site.register(Seance)
admin.site.register(Tache)