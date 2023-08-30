from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact (request):
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            theme = form.cleaned_data['theme']
            message = form.cleaned_data['message']
            
            email_to_send = EmailMessage (
                subject=theme,
                body=message,
                from_email=email,
                to=['dezsoszabolcs46@gmail.com'],
                reply_to=[email],
                headers={'Content-Type': 'text/plain'}
            )
            
            email_to_send.send()
            
            return render(request, 'contact_response.html', {'name':name, 'theme':theme})
        
        
    return render(request, 'contact.html', {'form':form})
