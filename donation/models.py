from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Linked to the built-in User model
    blood_group = models.CharField(max_length=3)
    organ_type= models.CharField(max_length=50)
    date_of_birth = models.DateField()
    health_status = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)
    
    # Additional fields from the second model
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.user.username} ({self.organ_type})"


class Recipient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    organ_needed = models.CharField(max_length=50)
    health_status = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Organ(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
