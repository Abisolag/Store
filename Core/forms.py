from django import forms
from .models import Products

class uploadform(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'description', 'minimum_order', 'price', 'stock', 'image']
