from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'hiuasdasd87687'})

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.POST.get('uppercase'):
        characters.extend('ABCDEFGHIJKMNOPQRSTUVWXYZ')
    
    if request.POST.get('numbers'):
        characters.extend('0123456789')
    
    if request.POST.get('specialchars'):
        characters.extend('!@#$%^)(*&')

    thepassword = ''
    length = int(request.POST.get('charlen', 12))
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password' : thepassword})

def about(request):
    return render(request, 'generator/about.html')
