from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    

class UserRoles(models.Model):
    role = models.CharField(max_length=100, unique=True)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    role = models.ForeignKey(UserRoles, on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    credit_card = models.CharField(max_length=100)

    
class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    

class AirlineCompany(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Flight(models.Model):
    airline_company = models.ForeignKey(AirlineCompany, on_delete=models.CASCADE, default='unknown')
    origin_country = models.ForeignKey(Country, related_name='departures', on_delete=models.CASCADE, default='unknown')
    destination_country = models.ForeignKey(Country, related_name='arrivals', on_delete=models.CASCADE, default='unknown')
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    remaining_tickets = models.IntegerField()


class Ticket(models.Model):
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    
    
    
    
    