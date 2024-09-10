"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.home, name='base'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('blog/blog1.html', views.blog1, name='blog1'),
    path('blog/blog2.html', views.blog2, name='blog2'),
    path('blog/blog4.html', views.blog4, name='blog4'),
    path('blog/blog3.html', views.blog3, name='blog3'),
    path('blog/blog5.html', views.blog5, name='blog5'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('saveEnquiry/', views.saveEnquiry,name="saveEnquiry"),
    
]

