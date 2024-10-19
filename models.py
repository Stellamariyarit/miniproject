from django.db import models
from django.contrib.auth.models import User  # Using the built-in User model
from django.utils import timezone

# Feedback model
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Donor model
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Linking to built-in User model
    blood_group = models.CharField(max_length=3)
    organ_type = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    health_status = models.TextField()
    date_registered = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Doctor model
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Linking to built-in User model
    specialization = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# Recipient model
class Recipient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Linking to built-in User model
    required_organ = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=3, default='Not Provided')
    date_of_birth = models.DateField()
    health_status = models.TextField()
    #date_registered = models.DateField(auto_now_add=True)
    date_registered = models.DateField(default='2024-01-01')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Donation Appointment model
class DonationAppointment(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return f"Appointment for {self.donor.user.username} at {self.hospital} on {self.date}"

#from django.db import models

class Donation(models.Model):
    donor = models.ForeignKey('Donor', on_delete=models.CASCADE)
    organ_type = models.CharField(max_length=100)
    #donation_date = models.DateField()
    donation_date = models.DateField(default=timezone.now)  # Set default to current date

    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Donation by {self.donor} of {self.organ_type}"
