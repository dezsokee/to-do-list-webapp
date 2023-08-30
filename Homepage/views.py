from turtle import done
from django.shortcuts import render, redirect
from . models import Action

def activities (request):
    actions = Action.objects.all()
    if request.method == "GET":
        return render(request, 'activities.html', {"actions": actions})
    elif request.method == "POST":
        if actions.done == 'on':
            actions.done = False
        return render(request, 'activities.html', {"actions": actions})

def new_activity (request):
    
    if request.method == "GET":
        return render(request, 'new_activity.html')
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
        
        return redirect('activities')
    

def homepage (request):
    return render(request, 'homepage.html')