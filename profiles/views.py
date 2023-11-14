from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .forms import ReservationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('booking')
        else:
            messages.error(request,
                           "There was an error logging in, please try again")
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,
                     "You have logged out succesfully")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,
                             "You have registered succesfully")
            return redirect('booking')
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {
        'form': form,
    })


def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            # Associate the reservation with the logged-in user
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            # Redirect to a success page or wherever you want
            return redirect('make_reservation')
    else:
        form = ReservationForm()

    return render(request, 'booking.html', {'form': form})
