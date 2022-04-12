from django.urls import path
from app import views
urlpatterns = [
    path('', views.index,name='index'),
    path('tache', views.tacheListDetailView.as_view(),name='tache-list'),
    path('tache/', views.tacheListDetailView.as_view(),name='tache-list'),
    path('tache/<int:pk>/',views.tacheDetailView.as_view(),name='tache-detail'),
]