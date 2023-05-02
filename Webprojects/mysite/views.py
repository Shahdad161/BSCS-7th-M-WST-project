from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Signup

def home(request):
    return render(request, "index.html")

def about(request):
    if request.method == 'POST':
        Signup.objects.create(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password'],
            confirmPassword=request.POST['confirmPassword']
        )
        return HttpResponseRedirect('/about/')
    else:
        return render(request, 'about.html')
