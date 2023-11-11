from django.shortcuts import render


def home(request):
    """ View to return to index page """
    return render(request, 'home.html', {})


def contacto(request):
    """ View to return to contact page """
    return render(request, 'contacto.html', {})


def booking(request):
    """ View to return to booking page """
    return render(request, 'booking.html', {})
