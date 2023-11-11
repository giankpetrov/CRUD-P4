from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contacto.html', views.contacto, name="contacto"),
    path('booking.html', views.booking, name="booking"),
]
