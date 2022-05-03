from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.fooldal, name='fooldal'),
    path('uj_szemely/', views.uj_szemely, name="uj_szemely"),
    path('tennivalok/', views.index, name="tennivalok"),
]
