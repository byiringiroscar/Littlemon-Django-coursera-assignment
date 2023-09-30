from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    return render(request, 'book.html')


def menu(request):
    foods = Menu.objects.all()
    context = {
        "foods": foods
    }
    return render(request, 'menu.html', context)
