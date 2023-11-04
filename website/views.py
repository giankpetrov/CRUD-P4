from django.shortcuts import render


def home(request):
    """ View to return to index page """
    return render(request, 'home.html', {})
