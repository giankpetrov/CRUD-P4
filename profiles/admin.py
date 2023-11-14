from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'date',
                    'time', 'no_of_people', 'special_request']
    search_fields = ['name', 'email', 'date']
    list_filter = ['date', 'time', 'no_of_people']
