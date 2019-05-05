from django.shortcuts import render
from .models import DatosPersonales



def index(request):
    return render(request,"Alumnos/index.html")

def res(request):
    Datos=DatosPersonales.objects.all()
    return render(request, "Alumnos/resultado.html",{"Alumnos":Datos})



