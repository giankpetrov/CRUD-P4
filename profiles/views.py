from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .forms import ReservationForm
from .models import Reservation

def is_superuser(user):
    return user.is_superuser

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reservation_list')
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
            messages.success(request,
                             "We have received your reservation")
            # Redirect to a success page or wherever you want
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    return render(request, 'make_reservation.html', {'form': form})

@login_required
def reservation_list(request):
    if request.user.is_superuser:
        reservations = Reservation.objects.all()
    else:
        reservations = Reservation.objects.filter(user=request.user)
        
    return render(request, 'reservation_list.html',
                  {'reservations': reservations})


def update_list(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    form = ReservationForm(request.POST or None, instance=reservation)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('reservation_list')

    return render(request, 'update_reservation.html',
                  {'reservation': reservation,
                   'form': form})


def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    reservation.delete()
    messages.success(request,
                            "We have delete your reservation")
        # Redirect to a success page or wherever you want
    return redirect('reservation_list')