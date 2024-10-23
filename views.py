from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserSignupForm, DonorForm, RecipientForm, DoctorForm
from django.views import View


def donor_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        donor_form = DonorForm(request.POST)
        if user_form.is_valid() and donor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            donor = donor_form.save(commit=False)
            donor.user = user
            donor.save()
            login(request, user)
            return redirect('login')  # Redirect to donor dashboard after signup
    else:
        user_form = UserSignupForm()
        donor_form = DonorForm()
    return render(request, 'donor_signup.html', {'user_form': user_form, 'donor_form': donor_form})

from django.contrib import messages

def recipient_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        recipient_form = RecipientForm(request.POST)
        
        if user_form.is_valid() and recipient_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            recipient = recipient_form.save(commit=False)
            recipient.user = user
            recipient.save()
            login(request, user)

            # Add a success message
            messages.success(request, 'Signup successful! Welcome to the system.')
            
            return redirect('login')
    else:
        user_form = UserSignupForm()
        recipient_form = RecipientForm()
    
    return render(request, 'recipient_signup.html', {
        'user_form': user_form,
        'recipient_form': recipient_form
    })


def doctor_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        doctor_form = DoctorForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.user = user
            doctor.save()
            login(request, user)
            return redirect('doctor_dashboard')  # Redirect to doctor dashboard after signup
    else:
        user_form = UserSignupForm()
        doctor_form = DoctorForm()
    return render(request, 'doctor_signup.html', {'user_form': user_form, 'doctor_form': doctor_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on user type
            if hasattr(user, 'donor'):
                return redirect('donor_dashboard')
            elif hasattr(user, 'recipient'):
                return redirect('recipient_dashboard')
            elif hasattr(user, 'doctor'):
                return redirect('doctor_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


class SpreadAwarenessView(View):
    def get(self, request):
        return render(request, 'spread_awareness.html')  
    

class SuccessStoriesView(View):
    def get(self, request):
        return render(request, 'success_stories.html')   
    

def find_matching_donors(required_organ, blood_group):
    return Donor.objects.filter(organ_type=required_organ, blood_group=blood_group)


def search_organ(request):
    if request.method == 'POST':
        required_organ = request.POST.get('required_organ')
        blood_group = request.POST.get('blood_group')
        matching_donors = find_matching_donors(required_organ, blood_group)
        return render(request, 'organ_results.html', {'donors': matching_donors})
    return render(request, 'search_organ.html')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def feedback(request):
    return render(request, 'feedback.html')


def doctor_profile(request):
     return render(request, 'doctor_profile.html')

def view_patients(request):
     return render(request, 'view_patients.html')

def schedule_appointments(request):
     return render(request, 'schedule_appointments.html')

from .models import Feedback  

def feedback_view(request):
    success = False
    feedback_list = Feedback.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Feedback.objects.create(name=name, email=email, message=message)
        success = True
        return redirect('feedback')  

    return render(request, 'feedback.html', {'success': success, 'feedback_list': feedback_list})


def submit_feedback(request):
    if request.method == 'POST':
 
        feedback_instance = Feedback(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        feedback_instance.save()
        return redirect('feedback')   
    


def donlogin(request):
    return render(request, 'donlogin.html')

from .models import Donor  
from django.contrib.auth.decorators import login_required


from .models import OrganRequest, Donation   

@login_required
def donor_dashboard(request):
    try:
        donor = Donor.objects.get(user=request.user)
        organ_requests = OrganRequest.objects.filter(donor=donor)   
        donations = Donation.objects.filter(donor=donor)   
        return render(request, 'donor_dashboard.html', {
            'donor': donor,
            'organ_requests': organ_requests,
            'donations': donations
        })
    except Donor.DoesNotExist:
        return render(request, 'donor_dashboard.html', {'error': 'Donor profile not found.'})



@login_required
def recipient_dashboard(request):
     return render(request, 'recipient_dashboard.html')
    

#def edit_profile(request):
 #    return render(request, 'edit_profile.html')   

def view_organ_requests(request):
     return render(request, 'view_organ_requests.html')

#def donation_history(request):
 #    return render(request, 'donation_history.html')

#@login_required
#def donation_history(request):
 #   donor = Donor.objects.get(user=request.user)
  #  donations = Donation.objects.filter(donor=donor)
   # return render(request, 'donation_history.html', {'donations': donations})


@login_required
def donation_history(request):
    donor = Donor.objects.get(user=request.user)
    donations = Donation.objects.filter(donor=donor)  # Retrieve the donor's donation history
    return render(request, 'donation_history.html', {
        'donations': donations
    })


from django.contrib.auth import logout

 
from .models import Recipient, OrganRequest, Donation

@login_required
def recipient_dashboard(request):
    try:
        # Fetch the recipient information using the logged-in user
        recipient = Recipient.objects.get(user=request.user)
        
        # Get recipient's organ requests
        organ_requests = OrganRequest.objects.filter(donor__user=request.user)
 

        # Get available donations (assuming organs that match recipient's needs)
        available_donations = Donation.objects.filter(organ_type=recipient.organ_needed)

        return render(request, 'recipient_dashboard.html', {
            'recipient': recipient,
            'organ_requests': organ_requests,
            'available_donations': available_donations,
        })
    except Recipient.DoesNotExist:
        # Handle the case where the recipient does not exist
        return render(request, 'recipient_dashboard.html', {'error': 'Recipient profile not found.'})


from .forms import OrganRequestForm
 
 
@login_required
def request_organ(request):
    try:
        # Try to fetch the donor object for the logged-in user
        donor = Donor.objects.get(user=request.user)
    except Donor.DoesNotExist:
        # Handle the case where the user is not a donor
        return render(request, 'error.html', {'message': 'You must have a donor profile to request an organ.'})
    
    if request.method == 'POST':
        form = OrganRequestForm(request.POST)
        if form.is_valid():
            organ_request = form.save(commit=False)
            organ_request.donor = donor
            organ_request.status = 'Pending'  # Set default status as Pending
            organ_request.save()
            return redirect('success_page')  # Redirect to a success page after submission
    else:
        form = OrganRequestForm()
    
    return render(request, 'request_organ.html', {'form': form})



def doctor_dashboard(request):
     return render(request, 'doctor_dashboard.html')



def match_donors_to_recipients():
    donors = Donor.objects.filter(availability=True)
    organ_requests = OrganRequest.objects.filter(status='Pending')

    matches = []
    
    # Iterate over each organ request and try to match with available donors
    for request in organ_requests:
        for donor in donors:
            # Match based on blood group and organ type
            if donor.blood_group == request.recipient.blood_group and donor.organ_type == request.organ_type:
                matches.append({
                    'recipient': request.recipient,
                    'donor': donor
                })
                # Mark donor as unavailable
                donor.availability = False
                donor.save()
                # Update organ request status
                request.status = 'Matched'
                request.save()
                break  # Move to the next organ request after finding a match

    return matches


def assign_organs(request):
    matches = match_donors_to_recipients()  

    return render(request, 'assign_organs.html', {'matches': matches})



@login_required
def toggle_availability(request):
    donor = Donor.objects.get(user=request.user)
    donor.availability = not donor.availability  # Toggle availability
    donor.save()
    return redirect('donor_dashboard')

 

# For recipient dashboard or doctor dashboard
def view_available_donors(request):
    available_donors = Donor.objects.filter(availability=True)  # Only donors marked as available
    return render(request, 'available_donors.html', {'available_donors': available_donors})

 

def available_donors_for_recipient(request):
    # Get only the donors who are available for donation
    available_donors = Donor.objects.filter(availability=True)
    return render(request, 'recipient_dashboard.html', {'available_donors': available_donors})


from .forms import RecipientProfileForm   
from .forms import DonorProfileForm   


def edit_donor_profile(request):
    donor = request.user.donor   
    if request.method == 'POST':
        form = DonorProfileForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_dashboard')  # Redirect to donor dashboard after saving
    else:
        form = DonorProfileForm(instance=donor)
    return render(request, 'edit_donor_profile.html', {'form': form})

def edit_recipient_profile(request):
    recipient = request.user.recipient  
    if request.method == 'POST':
        form = RecipientProfileForm(request.POST, instance=recipient)
        if form.is_valid():
            form.save()
            return redirect('recipient_dashboard')  # Redirect to recipient dashboard after saving
    else:
        form = RecipientProfileForm(instance=recipient)
    return render(request, 'edit_recipient_profile.html', {'form': form})


from .models import OrganAssignment  # Adjust the import according to your project structure


@login_required
def organ_assignments(request):
    # Assuming you have a model that relates recipients and donors
    matches = OrganAssignment.objects.filter(recipient__user=request.user)  # Adjust as per your model
    return render(request, 'organ_assignments.html', {'matches': matches})
