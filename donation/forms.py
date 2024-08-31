from django import forms
from .models import Donor
 

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'age', 'blood_group', 'contact_info', 
                   'organ_type', 'date_of_birth', 'health_status']

 