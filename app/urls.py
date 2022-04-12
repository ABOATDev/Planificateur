from django.urls import path
from app import views
urlpatterns = [
    path('', views.index,name='index'),

    # Tache : 
    path('tache/', views.tacheListDetailView.as_view(),name='tache-list'),
    path('tache/<int:pk>/',views.tacheDetailView.as_view(),name='tache-detail'),

    path('tacheByProjet/<int:pk>/',views.tacheByProjetListDetailView.as_view(),name='tacheByProjet-list'),

    
    # Personne : 
    path('personne/', views.personneListDetailView.as_view(),name='personne-list'),
    path('personne/<int:pk>/', views.personneDetailView.as_view(),name='personne-detail'),

    # Projet : 
    path('projet', views.projetListDetailView.as_view(),name='projet-list'),
    path('projet/', views.projetListDetailView.as_view(),name='projet-list'),
    path('projet/<int:pk>/',views.projetDetailView.as_view(),name='projet-detail'),


]