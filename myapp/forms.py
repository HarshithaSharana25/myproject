# contact/forms.py
from django import forms
from .models import contactEnquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactEnquiry
        fields = ('name', 'contact', 'email', 'text')
