from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'model_year', 'kilometres', 'color', 'engine_capacity', 
                  'fuel_type', 'doors', 'gearbox_type', 'price']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Brand'}),
            'model': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Model'}),
            'model_year': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Model Year'}),
            'kilometres': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Kilometres'}),
            'color': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Color'}),
            'engine_capacity': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Engine Capacity'}),
            'fuel_type': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Fuel Type'}),
            'doors': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Doors'}),
            'gearbox_type': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Gearbox Type'}),
            'price': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Price'}),
        }
