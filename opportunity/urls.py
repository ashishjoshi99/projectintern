"""opportunity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('opp.urls')),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.SignUp.as_view(), name='signup'),
    path('orgsignup/', views.OrganisationSignUp.as_view(), name='orgsignup'),
    path('userindex/', views.userindex.as_view(), name='userindex'),
     path('logout/', views.logout.as_view(), name='logout'),
     path('orgindex/', views.userindex.as_view(), name='orgindex'),
     path('addopportunity/', views.addOpportunity.as_view(), name='addOpportunity'),

]
