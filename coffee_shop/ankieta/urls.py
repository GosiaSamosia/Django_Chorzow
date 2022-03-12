import django


from django.urls import path

from ankieta.models import Odpowiedz
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('pytania/',views.pytania,name='pytania'),
    path('pytania/<int:pytanie_id>/',views.szczegoly,name='szczegoly'),
    path('pytania/<int:pytanie_id>/glosuj/<int:odpowiedz_id>',views.glosuj,name='glosuj')
    
]