from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('contacts/', views.contact, name='contact'),
]
