from django.shortcuts import render


def home(request):
    """ View to return to index page """
    return render(request, 'home.html', {})


def booking(request):
    """ View to return to booking page """
    return render(request, 'booking.html', {})
