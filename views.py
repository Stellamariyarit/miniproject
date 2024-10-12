from django.shortcuts import render, redirect
from .models import Donor, Recipient, Doctor
from django.contrib.auth import authenticate, login
from .forms import DonorSignupForm, RecipientSignupForm, DoctorSignupForm
from django.contrib.auth.decorators import login_required
from .models import Donor, Donation, DonationAppointment
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone
from .forms import DonorProfileForm, HealthStatusForm, OrganRequest # You'll need to create this f
from .forms import DonorForm  # Assuming you have a form class for donor data
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Donation
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





@login_required
def edit_profile(request):
    donor = Donor.objects.get(user=request.user)  # Fetch the current donor's data

    if request.method == 'POST':
        form = DonorForm(request.POST, request.FILES, instance=donor)  # Use DonorForm to update donor info
        if form.is_valid():
            form.save()  # Save updated donor info to the database
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('view_profile')  # Redirect to a page where the donor details are shown
    else:
        form = DonorForm(instance=donor)  # Prefill the form with the current donor info

    return render(request, 'edit_profile.html', {'form': form, 'donor': donor})





@login_required
def donor_login(request):
    donor = Donor.objects.get(user=request.user)  # Fetch the donor's profile
    donations = Donation.objects.filter(donor=donor).order_by('-date')  # List of past donations
    appointments = DonationAppointment.objects.filter(donor=donor, date__gte=timezone.now())  # Upcoming appointments

    context = {
        'donor': donor,
        'donations': donations,
        'appointments': appointments
    }
    
    return render(request, 'donor_login.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to login or some other page


# Home view
def home(request):
    return render(request, 'home.html')

# Donor List view
#def donor_list(request):
#    donors = Donor.objects.all()
 #   return render(request, 'donor_list.html', {'donors': donors})

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

#@login_required
#def recipient_dashboard(request):
 #   return render(request, 'recipient_dashboard.html')

#@login_required
#def doctor_dashboard(request):
 #   return render(request, 'doctor_dashboard.html')

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

@login_required
def check_organ_demand(request):
    available_organs = OrganRequest.objects.filter(is_active=True)  # Assuming OrganRequest model exists
    return render(request, 'organ_demand.html', {'available_organs': available_organs})

def organ_demand(request):
    # Your logic here
    return render(request, 'organ_demand.html')


#def login_view(request):
 #   if request.method == 'POST':
  #      username = request.POST.get('username')
   #     password = request.POST.get('password')
    #    user = authenticate(request, username=username, password=password)
        
     #   if user is not None:
      #      login(request, user)
            
            # Check the user_type and redirect to the appropriate dashboard
       #     if user.user_type == 'donor':
        #        return redirect('donor_dashboard')
         #   elif user.user_type == 'recipient':
          #      return redirect('recipient_dashboard')
           # elif user.user_type == 'doctor':
            #    return redirect('doctor_dashboard')
        #else:
            # Handle login failure (wrong username or password)
         #   return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    #return render(request, 'login.html')

 


#def login_view(request):
 #   if request.method == 'POST':
  #      email = request.POST['email']
   #     password = request.POST['password']
    #    #role = request.POST['role']  # e.g., 'donor', 'recipient', or 'doctor'

        # Authenticate the user
     #   user = authenticate(request, username=email, password=password)

      #  if user is not None:
       #     login(request, user)
            # Redirect based on the user's role
        #    if role == 'donor':
         #       return redirect('donor_login')  # Replace with the correct donor view
          #  elif role == 'recipient':
           #     return redirect('recipient_login')  # Replace with the correct recipient view
            #elif role == 'doctor':
             #   return redirect('doctor_login')  # Replace with the correct doctor view
        #else:
         #   messages.error(request, 'Invalid email or password.')

    #return render(request, 'login.html')


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

#def signup_view(request):
 #   if request.method == 'POST':
  #      form = CustomUserCreationForm(request.POST)
   #     if form.is_valid():
    #        user = form.save()
     #       login(request, user)
            
            # Ensure role is fetched correctly and redirect accordingly
      #      user_role = user.role.lower()  # Assuming 'role' is stored in lowercase, adjust as needed
            
            # Redirect based on user role
       #     if user_role == 'donor':
        #        return redirect('donor_dashboard')  # Replace with correct donor dashboard URL
         #   elif user_role == 'recipient':
          #      return redirect('recipient_dashboard')  # Replace with correct recipient dashboard URL
           # elif user_role == 'doctor':
            #    return redirect('doctor_dashboard')  # Replace with correct doctor dashboard URL
            #else:
             #   return redirect('default_dashboard')  # Default dashboard URL
    #else:
     #   form = CustomUserCreationForm()
    
    #return render(request, 'signup.html', {'form': form})

 

def donation_statistics(request):
    # Get counts for different statuses
    donated_count = Donation.objects.filter(status='donated').count()
    received_count = Donation.objects.filter(status='received').count()
    accepted_count = Donation.objects.filter(status='accepted').count()
    rejected_count = Donation.objects.filter(status='rejected').count()

    # Pass the statistics to the template
    context = {
        'donated_count': donated_count,
        'received_count': received_count,
        'accepted_count': accepted_count,
        'rejected_count': rejected_count
    }
    return render(request, 'donation_success.html', context)

@login_required
def view_profile(request):
    donor = Donor.objects.get(user=request.user)  # Fetch the current donor's data
    return render(request, 'view_profile.html', {'donor': donor})


