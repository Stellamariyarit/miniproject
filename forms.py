from django import forms
from django.contrib.auth.models import User
from .models import Donor, Recipient, Doctor

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

 

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['blood_group', 'organ_type', 'date_of_birth', 'health_status']

    date_of_birth = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Accepting date input in dd/mm/yyyy format
        widget=forms.DateInput(
            attrs={
                'type': 'text',  # Change to 'text' to use a placeholder
                'placeholder': 'dd/mm/yyyy',  # Placeholder for user guidance
            }
        )
    )


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['organ_needed', 'health_status']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'experience_years', 'contact_number']


from .models import OrganRequest

class OrganRequestForm(forms.ModelForm):
    class Meta:
        model = OrganRequest
        fields = ['organ_type', 'status']  # Only include fields you want to expose to the donor
        widgets = {
            'status': forms.HiddenInput(),  # Automatically set status as 'Pending'
        }

class RecipientProfileForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['health_status', 'organ_needed' ]  # Add any other fields you want to allow editing

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['blood_group', 'organ_type', 'health_status' ]  # Add any other fields you want to edit