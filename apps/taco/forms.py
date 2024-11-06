# apps/taco/forms.py
from django import forms

class TacoForm(forms.Form):
    param = forms.CharField(label='Param', max_length=100)
    amount = forms.IntegerField(label='Amount')