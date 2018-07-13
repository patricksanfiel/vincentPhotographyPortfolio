from django import forms
from django.forms import ModelForm, DateTimeField
from .models import ClientContact



class ClientContactForm(forms.ModelForm):
    class Meta:
        model = ClientContact
        fields = ['name','email','subject','message','budget','event_date']
        widgets = {
            'event_date': forms.DateTimeInput(attrs={ 'id':'date', 'class':'date', 'input_formats':["%m/%d/%Y h:mm TT"]}),
        }
