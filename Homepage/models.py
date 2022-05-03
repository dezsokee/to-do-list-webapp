from pyexpat import model
from django.db import models

class Action (models.Model):
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    whatdo = models.TextField()
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField()
    