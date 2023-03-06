from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import Country, User, Customer, AirlineCompany, Flight, Ticket

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] #im not sure about this 


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class CountryForm(ModelForm):
    class meta:
        model = Country
        fields = ['name']   #modify it 


class AirlineCreationForm(ModelForm):
    class Meta:
        model = AirlineCompany
        fields = '__all__'


class FlightCreationForm(ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'


class TicketCreationForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

