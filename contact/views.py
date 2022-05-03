from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage

def kapcsolat (request):
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nev = form.cleaned_data['nev']
            email = form.cleaned_data['email']
            tema = form.cleaned_data['tema']
            uzenet = form.cleaned_data['uzenet']
            
            email_to_send = EmailMessage (
                subject=tema,
                body=uzenet,
                from_email=email,
                to=['dezsoszabolcs46@gmail.com'],
                reply_to=[email],
                headers={'Content-Type': 'text/plain'}
            )
            
            email_to_send.send()
            
            return render(request, 'kapcsolat_valasz.html', {'nev':nev, 'tema':tema})
        
        
    return render(request, 'kapcsolat.html', {'form':form})
