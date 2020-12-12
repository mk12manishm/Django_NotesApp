"""FINALONE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from NEWapp.views import editor,User_Login,First_Page,register,Login,destroy,logout
from NEWapp import views
urlpatterns = [
    
    path('editor/',editor),
    path('admin/', admin.site.urls),
    path('User_Login/',User_Login),
    path('',First_Page),
    path('register/',register),
    path('Login/',Login),
    path('destroy/<int:id>',views.destroy),
    path('logout/',logout)
   
]
