from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Reservation
from django.conf import settings


class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        help_text="Enter the date in dd-mm-yyyy format"
    )

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time',
                  'no_of_people', 'special_request']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, classes, or placeholders if needed
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['time'].widget.attrs['class'] = 'form-control'
        self.fields['no_of_people'].widget.attrs['class'] = 'form-control'
        self.fields['special_request'].widget.attrs['class'] = 'form-control'
        # Add similar lines for other fields as needed


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
