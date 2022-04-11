from django.shortcuts import render

from Familiares.models import Familiar

# Create your views here.

def inicio (request):

    return render(request, "Familiares/inicio.html")

def familiares (request):

    familiar = Familiar.objects.all()

    return render(request, "Familiares/familiares.html", {"familiares":familiar})