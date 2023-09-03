from django.contrib import admin 
from django.urls import path, include 

urlpatterns = [
    path("admin/", admin.site.urls),
    #sE HACE REFERENCIA A UN ARCHIVO EXTERNO QUE CONTENDRA URLS QUE SERAN USADAS
    path('', include('tasks.urls')),

]
