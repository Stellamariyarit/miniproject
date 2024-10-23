from django.db import models
from django.contrib.auth.models import User

# Feedback model
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, default=1)  # Example default
 
    blood_group = models.CharField(max_length=3)
    organ_type = models.CharField(max_length=50)
    availability = models.BooleanField(default=False)  # Add this field if not already present

    date_of_birth = models.DateField()
    health_status = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

class Recipient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organ_needed = models.CharField(max_length=50)
    health_status = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField(default=0)
    #contact_number = models.CharField(max_length=15, default='0000000000')
    contact_number = models.CharField(max_length=15, default='')



#from django.db import models
 

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, null=True, blank=True)  # Tracks recipient (optional if null)
    organ_type = models.CharField(max_length=100)
    donation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')  # Tracks the status of the donation


class OrganRequest(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, default=1)  # Assuming you have a Donor with ID 1
    organ_type = models.CharField(max_length=100)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)


class OrganAssignment(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    organ_type = models.CharField(max_length=100)
    assignment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.user.username} -> {self.recipient.user.username} ({self.organ_type})"