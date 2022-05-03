from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('kapcsolatok/', views.kapcsolat, name='kapcsolat'),
]
