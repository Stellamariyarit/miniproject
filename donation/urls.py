from django.urls import path
from . import views
from .views import donor_signup, recipient_signup, doctor_signup
from .views import organ_demand
from .views import donor_login, recipient_login, doctor_login
from django.conf import settings
from django.conf.urls.static import static
from .views import donor_signup  # Assuming the view is named donor_signup
 
 


urlpatterns = [
    path('', views.home, name='home'),
    #path('donors/', views.donor_list, name='donor_list'),
    #path('login/', views.login_view, name='login'),
    #path('login/', views.login_view, name='login_view'),

    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    #path('signup/donor/', views.signup_donor, name='signup_donor'),  # Correct path
    #path('signup/donor/', views.donor_signup, name='donor_signup'),

    path('donor/signup/', donor_signup, name='donorsignup'),

    #path('recipient/signup/', recipient_signup, name='recipientsignup'),

    path('recipient/signup/reclogin', views.recipient_signup, name='recipientsignup'),
    path('reclogin/', views.reclogin, name='reclogin'),
    # Other URL patterns

    path('doctor/profile/', views.doctor_profile, name='doctor_profile'),
    path('doctor/patients/', views.view_patients, name='view_patients'),
    path('doctor/schedule_appointments/', views.schedule_appointments, name='schedule_appointments'),



    #path('recipient/signup/', views.recipient_signup, name='recipientsignup'),
    #path('recipient/login/', views.recipient_login, name='reclogin'),  # Ensure this line exists
    path('donlogin/', views.donlogin, name='donlogin'),  # Ensure this line exists
    path('doclogin/', views.doclogin, name='doclogin'),  # Ensure this is correct
    path('doctor/signup/doclogin', views.doctor_signup, name='doctorsignup'),  # Ensure this is defined
    #path('doctor/login/', views.doctor_login, name='doclogin'),  # Ensure this is defined
    #path('recipient/signup/', views.recipient_signup, name='recipientsignup'),
    path('recipient/login/', views.recipient_login, name='recipientlogin'),


    #path('recipient/signup/reclogin/', recipient_login, name='recipient_login'),  # Adjust as needed
    #path('doctor/signup/doclogin/', doctor_login, name='doctor_login'),  # Adjust as needed



    #path('signup/doctor/', doctor_signup, name='signup_doctor'),
    path('donor_login/', views.donor_login, name='donor_login'),
    path('recipient_login/', views.recipient_login, name='recipient_login'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('update_health_status/', views.update_health_status, name='update_health_status'),
    path('check_organ_demand/', views.check_organ_demand, name='check_organ_demand'),
    #path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('organ_demand/', organ_demand, name='organ_demand'),
    path('donation/success/', views.donation_statistics, name='donation_statistics'),
    path('login/', views.login_view, name='login'),  # Ensure this exists


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
 