from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_type', 'address', 'landlord', 'neighbourhood', 'zip_code', 'description', 'price', 'bedrooms',
                  'bathrooms', 'image']
