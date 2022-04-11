from django.urls import path

from Familiares import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Familiares', views.familiares, name="Familiares")
]
