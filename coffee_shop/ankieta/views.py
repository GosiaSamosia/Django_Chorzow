from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pytanie
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("To jest strona mojej aplikacji!!!")


def pytania(request):
    # return HttpResponse("To są wszystkie pytania")
    lista_ostatnich_pytan=Pytanie.objects.all()[:5]
    return render(request,'ankieta\pytania.html',{'lista_ostatnich_pytan':lista_ostatnich_pytan})


def szczegoly(request, pytanie_id):
    pytanie=get_object_or_404(Pytanie, pk=pytanie_id)
    return render(request, 'ankieta/szczegoly.html',{'pytanie':pytanie})


def wyniki(request,pytanie_id):
    return HttpResponse(f"To są wyniki pytania {pytanie_id}")

def glosuj(request, pytanie_id, odpowiedz_id):
    return HttpResponse(f"To jest glosowanie {pytanie_id}, {odpowiedz_id}")

