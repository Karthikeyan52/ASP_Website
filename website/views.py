from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import model
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    data = model.Enquiry.object.all()
    context = {'data': data}
    if request.method == 'POST':
        x = model.Enquiry(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            contact=request.POST.get('contact'),
            subject=request.POST.get('subject')
        )
        if x is not None:
            x.save()
    return render(request, 'contact.html', context)
