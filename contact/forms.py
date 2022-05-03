from logging import PlaceHolder
from django import forms

temak = [('egyéb', 'Egyéb'), ('reklamáció', 'Reklamáció'),('megkeresés', 'Megkeresés'), ('tájékoztatás', 'Tájékoztatás')]

class ContactForm(forms.Form):
    nev = forms.CharField(max_length=50, label="Név", widget=forms.TextInput(attrs={'placeholder': 'Írja be a nevét!'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Írja be az e-mail címét!'}))
    tema = forms.ChoiceField(choices=temak, label="Téma")
    uzenet = forms.CharField(label="Üzenet", widget=forms.Textarea(attrs={'placeholder': 'Írjon nekünk...'}))