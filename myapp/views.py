from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import contactEnquiry
from .forms import ContactForm

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request,'blog3.html')

def blog4(request):
    return render(request,'blog4.html')

def blog5(request):
    return render(request,'blog5.html')

def contact(request):
    return render(request, 'contact.html')


def saveEnquiry(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            en = form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')