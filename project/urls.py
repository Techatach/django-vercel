"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("department/", views.department, name="department"),
    path("department_single/", views.department_single, name="department_single"),
    path("doctor/", views.doctor, name="doctor"),
    path("doctor_single/", views.doctor_single, name="doctor_single"),
    path("appointment/", views.appointment, name="appointment"),
    path("blog_sidebar/", views.blog_sidebar, name="blog_sidebar"),
    path("blog_single/", views.blog_single, name="blog_single"),
    path("contact/", views.contact, name="contact"),
    
    path("main/", views.main, name="main"),
    path("ai/", views.ai, name="ai"),
    path("heart_form/", views.heart_form, name="heart_form"),
    path("heart_result/", views.heart_result, name="heart_result"),
]
