from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.IntegerField(choices=[
        (9, '9AM'),
        (10, '10AM'),
        (11, '11AM'),
        (12, '12M'),
        (13, '1PM'),
        (14, '2PM'),
        (15, '3PM'),
        (16, '4PM'),
        (17, '5PM'),
        (18, '6PM'),
    ])
    no_of_people = models.IntegerField(choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ])
    special_request = models.TextField(blank=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time} \
                with {self.no_of_people} people"
