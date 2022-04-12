from django.urls import path
from app import views
urlpatterns = [
    path('', views.index,name='index'),
    path('list/', views.tacheListDetailView.as_view(),name='tache-list'),
]