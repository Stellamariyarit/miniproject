from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    #contact = models.CharField(max_length=15)
    #address = models.TextField()
    password = models.CharField(max_length=128)  # You might want to hash this

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Ensure this name is unique
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Ensure this name is unique
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )




    #email = models.EmailField(unique=True)
  #  role = models.CharField(max_length=20, choices=[
   #     ('donor', 'Donor'),
    #    ('recipient', 'Recipient'),
     #   ('doctor', 'Doctor'),
    #])

    # Specify related_name to avoid clashes
    #groups = models.ManyToManyField(
     #   'auth.Group',
      #  related_name='customuser_set',  # Change related_name to avoid clash
       # blank=True,
        #help_text=('The groups this user belongs to. A user will get all permissions '
         #           'granted to each of their groups.'),
        #verbose_name=('groups'),
    #)

    #user_permissions = models.ManyToManyField(
     #   'auth.Permission',
      #  related_name='customuser_set',  # Change related_name to avoid clash
       # blank=True,
        #help_text=('Specific permissions for this user.'),
        #verbose_name=('user permissions'),
    #)

    def __str__(self):
        return self.username








#class CustomUser(AbstractUser):
 #   username = models.CharField(max_length=150, unique=True)
  #  email = models.EmailField(unique=True)
    #contact = models.CharField(max_length=15)
    #address = models.TextField()
   # password = models.CharField(max_length=128)  # You might want to hash this
    # Add any additional fields you want for your custom user model

    #def __str__(self):
     #   return self.username


class OrganRequest(models.Model):
    organ_type = models.CharField(max_length=100)
    requested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    priority_level = models.CharField(max_length=50, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    date_requested = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.organ_type} requested by {self.requested_by}'


class Donation(models.Model):
    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organ_type = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[('donated', 'Donated'), ('received', 'Received'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='donated'
    )
    date = models.DateField(default=timezone.now)

# Donor model
class Donor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    organ_type = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    health_status = models.TextField()
    date_registered = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Recipient model
class Recipient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    required_organ = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    health_status = models.TextField()

    def __str__(self):
        return self.user.username

# Doctor model
class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class DonationAppointment(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    hospital = models.CharField(max_length=100)
