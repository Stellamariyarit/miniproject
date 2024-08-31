from django.urls import path
from . import views
from .views import loginn
 

urlpatterns = [
    path('register/', views.donor_registration, name='donor_registration'),
    path('success/', views.donor_success, name='donor_success'),
    path('search/', views.organ_search, name='organ_search'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.loginn, name='login'),
    path('signup/', views.signup, name='signup'),
    #path('userlogin/', views.loginn, name='userlogin')
    path('', views.home, name='home'),
    
]

 