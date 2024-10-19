from django.shortcuts import render, redirect
from .models import Donor, Recipient, Doctor
from django.contrib.auth import authenticate, login
from .forms import DonorSignupForm, RecipientSignupForm, DoctorSignupForm
from django.contrib.auth.decorators import login_required
from .models import Donation, DonationAppointment
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone
from .forms import DonorProfileForm, HealthStatusForm 
from django.contrib import messages
#from .models import Donation
from .models import Feedback  # Assuming you have a Feedback model

def feedback_view(request):
    success = False
    feedback_list = Feedback.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Create a new feedback entry
        Feedback.objects.create(name=name, email=email, message=message)
        success = True
        return redirect('feedback')  # Redirect to the same page to show success message

    return render(request, 'feedback.html', {'success': success, 'feedback_list': feedback_list})


def submit_feedback(request):
    if request.method == 'POST':
        # Logic to process feedback submission
        # You can save the feedback to the database here
        feedback_instance = Feedback(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        feedback_instance.save()
        return redirect('feedback')  # Redirect back to the feedback page after submission


def edit_profile(request):
    # Your logic for editing profile
    return render(request, 'edit_profile.html')  # Replace with the correct template


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to login or some other page


# Home view
def home(request):
    return render(request, 'home.html')


# Login view
def login_view(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def feedback(request):
    return render(request, 'feedback.html')

def signup(request):
    return render(request, 'signup.html')
 
def donor_login(request):
    return render(request, 'donor_login.html')

 
def recipient_login(request):
    return render(request, 'recipient_login.html')
 
def doctor_login(request):
    return render(request, 'doctor_login.html')

 

# Donor signup view
def donor_signup(request):
    if request.method == 'POST':
        form = DonorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Donor.objects.create(
                user=user,
                blood_group=form.cleaned_data.get('blood_group'),
                organ_type=form.cleaned_data.get('organ_type'),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                health_status=form.cleaned_data.get('health_status'),
            )
            login(request, user)
            return redirect('home')  # Redirect to home after signup
    else:
        form = DonorSignupForm()
    return render(request, 'donorsignup.html', {'form': form})

# Recipient signup view
def recipient_signup(request):
    if request.method == 'POST':
        form = RecipientSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Recipient.objects.create(
                user=user,
                required_organ=form.cleaned_data.get('required_organ'),
                blood_group=form.cleaned_data.get('blood_group'),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
                health_status=form.cleaned_data.get('health_status'),
            )
            login(request, user)
            return redirect('home')  # Redirect to home after signup
    else:
        form = RecipientSignupForm()
    return render(request, 'recipientsignup.html', {'form': form})

   



# Doctor signup view
def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Doctor.objects.create(
                user=user,
                specialization=form.cleaned_data.get('specialization'),
                hospital=form.cleaned_data.get('hospital'),
            )
            login(request, user)
            return redirect('home')  # Redirect to home after signup
    else:
        form = DoctorSignupForm()
    return render(request, 'doctorsignup.html', {'form': form})

@login_required
def update_health_status(request):
    donor = Donor.objects.get(user=request.user)
    if request.method == 'POST':
        form = HealthStatusForm(request.POST, instance=donor)  # You'll need to create this form
        if form.is_valid():
            form.save()
            return redirect('donor_login')
    else:
        form = HealthStatusForm(instance=donor)
    return render(request, 'update_health_status.html', {'form': form})

 
def organ_demand(request):
    # Your logic here
   return render(request, 'organ_demand.html')


 

def donlogin(request):
    return render(request, 'donlogin.html')

def reclogin(request):
    return render(request, 'reclogin.html')

def doclogin(request):
    return render(request, 'doclogin.html')

def doctor_profile(request):
    # logic to handle the doctor profile page
    return render(request, 'doctor_profile.html')

def view_patients(request):
    # Logic to display a list of patients or relevant info
    return render(request, 'view_patients.html')

def schedule_appointments(request):
    # Logic to handle appointment scheduling
    return render(request, 'schedule_appointments.html')


@login_required
def view_profile(request):
    donor = Donor.objects.get(user=request.user)  # Fetch the current donor's data
    return render(request, 'view_profile.html', {'donor': donor})


from django import forms


class DonorSignupForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['user', 'blood_group', 'organ_type', 'date_of_birth', 'health_status']

class RecipientSignupForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['user', 'required_organ', 'blood_group', 'date_of_birth', 'health_status']

class DoctorSignupForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['user', 'specialization', 'hospital']