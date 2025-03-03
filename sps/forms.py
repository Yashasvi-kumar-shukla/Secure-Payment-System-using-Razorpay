from django import forms
from .models import User

class ComfyPaymentForm(forms.Form):
    name = forms.CharField(max_length=100)
    amount = forms.CharField(max_length=100)
    