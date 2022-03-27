from multiprocessing import context
from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import osoba,adres,recepta,przepisane_leki

# Create your views here.

def index(request):
    dane=recepta.objects.order_by("-data_wystawienia")
    
    context={'tytul': 'Moja aplikacja medyczna',
             'lista_recept': dane} 
    return render(request,'recepta/index.html',context)