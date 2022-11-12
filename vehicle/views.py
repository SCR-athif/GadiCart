from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,BikeForm,CarForm,OtherForm,ReportForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')


def about(request):
    return render(request, 'users/about.html')




def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def car_view(request):
    vehicle = Car.objects.all()
    context = {
        'vehicle':vehicle,
    }
    return render(request, 'users/car_view.html', context)



def bike_view(request):
    vehicle = Bike.objects.all()
    context = {
        'vehicle':vehicle,
    }
    return render(request, 'users/bike_view.html', context)


def other_view(request):
    vehicle = Other.objects.all()
    context = {
        'vehicle':vehicle,
    }
    return render(request, 'users/bike_view.html', context)

def bdetails(request, id):
    details = Bike.objects.filter(ID=id).first()
    context={
        'vehicle':details
    }
    return render(request, 'users/details.html',context)

def cdetails(request, id):
    details = Car.objects.filter(ID=id).first()
    context={
        'vehicle':details
    }
    return render(request, 'users/details.html',context)

def odetails(request, id):
    details = Other.objects.filter(ID=id).first()
    context={
        'vehicle':details
    }
    return render(request, 'users/details.html',context)



@login_required()
def profile(request):
    return render(request, 'users/profile.html')


def sell(request):
    return render(request, 'users/sell.html')

def car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful, Your car selling add is posted.')
            return redirect('home')
    else:
        form = BikeForm()

    return render(request, 'users/car.html',  {'form':form})


def bike(request):
    if request.method == "POST":
        form = BikeForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful, Your bike selling add is posted.')
            return redirect('home')
    else:
        form = BikeForm()
    return render(request, 'users/bike.html',  {'form':form})


def other(request):
    if request.method == "POST":
        form = OtherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            vehicle=form.cleaned_data.get('Vehicle_Type')
            messages.success(request, f'Successful, Your {vehicle} selling add is posted.')
            return redirect('home')
    else:
        form = OtherForm()

    return render(request, 'users/other.html', {'form': form})


def contact(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('Name')
            messages.success(request, f'{name},Thank you for your report we will contact you soon')
            return redirect('home')
    else:
        form = ReportForm()

    return render(request, 'users/contact.html', {'form': form})