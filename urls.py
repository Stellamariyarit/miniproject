from django.urls import path
from . import views
from .views import SpreadAwarenessView, SuccessStoriesView  
from .views import donor_signup, recipient_signup, doctor_signup, login_view
from django.conf import settings
from django.conf.urls.static import static
from .views import search_organ 
from .views import donor_dashboard   
#from .views import edit_profile   
from .views import view_organ_requests  
from .views import donation_history  
from django.contrib.auth.views import LogoutView  
from django.contrib.auth import views as auth_views
from .views import recipient_dashboard  
from .views import edit_donor_profile, edit_recipient_profile


urlpatterns = [
    path('', views.home, name='home'),
    path('success-stories/', SuccessStoriesView.as_view(), name='success_stories'),   
    path('spread-awareness/', SpreadAwarenessView.as_view(), name='spread_awareness'),  


    path('donor_signup/', donor_signup, name='donor_signup'),
    path('recipient_signup/', recipient_signup, name='recipient_signup'),
    path('doctor_signup/', doctor_signup, name='doctor_signup'),
 
     #path('edit_profile/', edit_profile, name='edit_profile'),  
 
    path('view_organ_requests/', view_organ_requests, name='view_organ_requests'),  # Define the URL pattern
 
    path('donation_history/', donation_history, name='donation_history'),
    path('logout/', LogoutView.as_view(next_page='donor_dashboard'), name='logout'),
    path('login/', views.login_view, name='login'),  
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),


  
    path('recipient_dashboard/', recipient_dashboard, name='recipient_dashboard'),
    path('request-organ/', views.request_organ, name='request_organ'),

 

    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
 

    path('doctor/profile/', views.doctor_profile, name='doctor_profile'),
    path('doctor/patients/', views.view_patients, name='view_patients'),
    path('doctor/schedule_appointments/', views.schedule_appointments, name='schedule_appointments'),
    path('donor_dashboard/', donor_dashboard, name='donor_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('assign_organs/', views.assign_organs, name='assign_organs'),

 
    path('donlogin/', views.donlogin, name='donlogin'),  
 
    path('search_organ/', search_organ, name='search_organ'),
 
    path('feedback/submit/', views.submit_feedback, name='submit_feedback'),   
    path('request-organ/', views.request_organ, name='request_organ'),
    path('toggle_availability/', views.toggle_availability, name='toggle_availability'),
    path('available_donors/', views.view_available_donors, name='available_donors'),
    path('recipient_dashboard/', views.available_donors_for_recipient, name='recipient_dashboard'),
    path('edit_donor_profile/', edit_donor_profile, name='edit_donor_profile'),
    path('edit_recipient_profile/', edit_recipient_profile, name='edit_recipient_profile'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
 