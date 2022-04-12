from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Personne)
admin.site.register(Projet)
admin.site.register(Tache)


# from django.apps import apps


# models = apps.get_models()

# for model in models:
#     admin.site.register(model)