from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Donor, Recipient, Doctor#, OrganRequest

# Custom user signup forms with additional profile fields
class DonorSignupForm(UserCreationForm):
    blood_group = forms.CharField(max_length=3)
    organ_type = forms.CharField(max_length=50)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, 2025)))
    health_status = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'blood_group', 'organ_type', 'date_of_birth', 'health_status']

class RecipientSignupForm(UserCreationForm):
    required_organ = forms.CharField(max_length=50)
    blood_group = forms.CharField(max_length=3)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, 2025)))
    health_status = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'required_organ', 'blood_group', 'date_of_birth', 'health_status']

class DoctorSignupForm(UserCreationForm):
    specialization = forms.CharField(max_length=100)
    hospital = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',  'specialization', 'hospital']

# Forms to update specific profile models after signup
class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['blood_group', 'organ_type', 'date_of_birth', 'health_status', 'profile_picture']  # Profile picture is editable

class RecipientProfileForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['required_organ', 'date_of_birth', 'health_status']

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'hospital']

# OrganRequest form
#class OrganRequestForm(forms.ModelForm):
 #   class Meta:
  #      model = OrganRequest
   #     fields = ['organ_type', 'priority_level']

# Health status form to allow donors to update their health status
class HealthStatusForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['health_status']

 