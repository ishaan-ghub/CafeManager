from django import forms
from .models import beverage


class beverageform(forms.Form):
    beverage = forms.ModelChoiceField(queryset=beverage.objects.all(), label= 'Select the beverage here')