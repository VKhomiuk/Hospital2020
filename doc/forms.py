from django import forms
from .models import Reception

class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ('name', 'phone', 'email', 'msg')
