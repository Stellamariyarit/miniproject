from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Donor, Recipient, Organ
from .forms import DonorForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
 
 

def donor_registration(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_success')
    else:
        form = DonorForm()
    return render(request, 'donation/donor_registration.html', {'form': form})

def donor_success(request):
    return render(request, 'donation/donor_success.html')

def organ_search(request):
    organs = Organ.objects.filter(recipient__isnull=True)
    return render(request, 'donation/organ_search.html', {'organs': organs})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def feedback(request):
    return render(request, 'feedback.html')

def loginn(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

 
 # donation/views.py


def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or another page after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'signup.html')
