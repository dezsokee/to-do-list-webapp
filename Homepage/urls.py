from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('new_activity/', views.new_activity, name="new_activity"),
    path('activities/', views.activities, name="activities"),
]
