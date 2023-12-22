# services/forms.py
from django import forms
from .models import IceCreamService

class IceCreamServiceForm(forms.ModelForm):
    class Meta:
        model = IceCreamService
        fields = ['name', 'description']
