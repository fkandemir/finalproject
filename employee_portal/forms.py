from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
    ]
    GEARBOX_CHOICES = [
        ('Auto', 'Auto'),
        ('Manual', 'Manual'),
    ]
    fuel_type = forms.ChoiceField(choices=FUEL_CHOICES, widget=forms.Select(attrs={'class': 'input-field'}))
    gearbox_type = forms.ChoiceField(choices=GEARBOX_CHOICES, widget=forms.Select(attrs={'class': 'input-field'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input-field'}))  # Add a FileField for image upload

    class Meta:
        model = Car
        fields = ['brand', 'model', 'model_year', 'kilometres', 'color', 'engine_capacity', 
                  'fuel_type', 'doors', 'gearbox_type', 'price', 'image']  # Add 'image' to fields
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Brand'}),
            'model': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Model'}),
            'model_year': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Model Year'}),
            'kilometres': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Kilometres'}),
            'color': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Color'}),
            'engine_capacity': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Engine Capacity'}),
            'doors': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Doors'}),
            'price': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Price'}),
        }
