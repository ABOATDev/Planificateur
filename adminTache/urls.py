from django.urls import path
from adminTache import views
urlpatterns = [
    path('', views.index,name='index'),
    path('list/', views.tacheListDetailView.as_view(),name='tache-list'),
    path('<int:pk>/',views.tacheDetailView.as_view(),name='tache-detail'),
    path('matiere/<str:matiere_titre>/',views.matiere,name='matiere'),
    path('todo/<int:tache_a_faire>/',views.toDoList,name='todo')
]