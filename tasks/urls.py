from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list,name='task_list'),
    # Se debe de tener cuidado a la hora de implementar una ruta ya que si no terminas la ruta con un slash 
    # este producira un error     
    path('sumar/<int:a>/<int:b>/', views.sumar,name='sumar'),
    path('multiplicar/<int:a>/<int:b>/', views.multiplicar,name='multiplicar'),
    path('restar/<int:a>/<int:b>/', views.restar,name='restar'),
    path('potencia/<int:a>/<int:b>/', views.potencia, name='potencia'),

]

