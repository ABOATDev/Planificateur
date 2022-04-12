from django.urls import path
from app import views
urlpatterns = [
    path('', views.index,name='index'),
    path('list/', views.tacheListDetailView.as_view(),name='tache-list'),
    path('tache/', views.tacheListDetailView.as_view(),name='tache-list'),
    path('tache/<int:pk>/',views.tacheDetailView.as_view(),name='tache-detail'),
    path('personne/', views.personneListDetailView.as_view(),name='personne-list'),
    path('personne/<int:pk>/', views.personneDetailView.as_view(),name='personne-detail'),
]