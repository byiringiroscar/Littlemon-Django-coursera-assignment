from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import BookForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "book done")
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'book.html', {"form": form})


def menu(request):
    foods = Menu.objects.all()
    context = {
        "foods": foods
    }
    return render(request, 'menu.html', context)


def menu_detail(request, id):
    food = get_object_or_404(Menu, id=id)
    context = {
        "food": food
    }
    return render(request, 'menu_detail.html', context)
