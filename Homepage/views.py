from turtle import done
from django.shortcuts import render, redirect
from . models import Action
##from django.core.mail import send_email

def index (request):
    actions = Action.objects.all()
    if request.method == "GET":
        return render(request, 'index.html', {"actions": actions})
    elif request.method == "POST":
        if actions.done == 'on':
            actions.done = False
        return render(request, 'index.html', {"actions": actions})

def uj_szemely (request):
    
    if request.method == "GET":
        return render(request, 'uj_szemely.html')
    elif request.method == "POST":
        surname = request.POST.get('surname')
        lastname = request.POST.get('lastname')
        whatdo = request.POST.get('whatdo')
        done = request.POST.get('done')
        created = request.POST.get('created')
        deadline = request.POST.get('deadline')
        
        if done == 'on':
            done = True
        else:
            done = False
            
        formaction = Action(surname=surname, lastname=lastname, whatdo=whatdo, done=done, created=created, deadline=deadline)
        formaction.save()
        
        return redirect('tennivalok')
    

def fooldal (request):
    return render(request, 'fooldal.html')