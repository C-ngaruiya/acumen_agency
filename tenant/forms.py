from django import forms
from .models import Tenant


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'zip_code']
