from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'unit', 'stock', 'image']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }