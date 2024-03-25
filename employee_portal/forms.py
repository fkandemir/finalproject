from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'model_year']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Brand'}),
            'model': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Model'}),
            'model_year': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Model Year'}),
        }
