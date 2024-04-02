from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import model
from django.contrib import messages


def home(request):
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
    return render(request, 'home.html', context)


def login_user(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
            )
        if user is not None:
            login(request, user=user)
            return redirect('read')
    return render(request, 'login_page.html')