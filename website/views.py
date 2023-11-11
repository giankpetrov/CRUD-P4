from django.shortcuts import render


def home(request):
    """ View to return to index page """
    return render(request, 'home.html', {})


def contacto(request):
    """ View to return to index page """
    return render(request, 'contacto.html', {})
