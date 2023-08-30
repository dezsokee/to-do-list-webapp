from logging import PlaceHolder
from django import forms

temak = [('other', 'Other'), ('complaint', 'Complaint'),('business request', 'Business request'), ('information', 'Information')]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name", widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    theme = forms.ChoiceField(choices=temak, label="Theme")
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'placeholder': 'Send your opinion...'}))