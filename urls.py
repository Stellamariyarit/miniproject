"""
URL configuration for organ_donation_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from donation import views  # Import the view you created

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('donation.urls')),
    #path('donation/', include('donation.urls')),
    path('', views.home, name='home'), 
    path('signup', views.signup, name='signup'),
    path('login/', views.loginn, name='login'),
    path('', views.index, name='home'),
    #path('about/', views.about, name='about'),
    #path('index/', views.about, name='index'),
    #path('feedback/', views.about, name='feedback'),
    #path('contact/', views.about, name='contact'),
]


 