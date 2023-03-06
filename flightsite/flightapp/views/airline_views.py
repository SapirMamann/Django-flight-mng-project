from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from ..models import AirlineCompany, Country, User, Flight
from flightapp.forms import UserCreationForm, AirlineCreationForm, FlightCreationForm
from flightapp.facades.airline_facade import AirlineFacade
from flightapp.dal.airline_dal import AirlineDal


def airline_index(request):
    """
    Home page of an airline company
    """
    return render(request, 'flightapp/airline_index.html')


def airline_register(request):
    """
    Registration of a new airline company,
    needs to be modified
    """
    form = AirlineCreationForm
    form2 = UserCreationForm
    # if request.method == "POST":
    context = {'form': form, 'form2': form2}
    return render(request, 'flightapp/airline_register.html', context)
    

def airlines_list(request):
    """
    List of all airlines.
    goes to the relevant facade -> and the facade gets the data from the dal module
    """
    facade = AirlineFacade()
    airlines = facade.get_all_airlines()
    context = {'airlines': airlines} 
    return render(request, 'flightapp/airlines_list.html', context)


def airline_detail(request):
    """
    A specific airline (by name)
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            airline = AirlineCompany.objects.get(name=name)  #add a try except and a validation for user input. 
            airline.name.lower()
            print(airline)

            context = {'airline': airline}
            return render(request, 'flightapp/airline_detail.html', context)
        except Exception as e:
            return HttpResponse(f'airline doesnt exist, exception details: {e}')
    else:
        return render(request, 'flightapp/airline_detail.html')
    

def flights_list(request):
    """
    List of all flights 
    needs to be filtered by airline company and only relevant flights
    """
    flights = Flight.objects.all()
    context = {'flights': flights}
    return render(request, 'flightapp/flights_list.html', context)

def add_flight(request):
    """
    Adding a flight. 
    Only an admin/airline company can add flights.
    """
    form = FlightCreationForm()
    if request.method == 'POST':  
        airline_company = AirlineCompany.objects.get(id=request.POST.get('airline_company'))
        origin_country = Country.objects.get(id=request.POST.get('origin_country'))
        destination_country = Country.objects.get(id=request.POST.get('destination_country'))

        new_flight = Flight.objects.create(                         #creating a new flight instance with all of its required fields
            airline_company=airline_company,
            origin_country=origin_country,
            destination_country=destination_country,
            departure_time=request.POST.get('departure_time'),
            landing_time=request.POST.get('landing_time'),
            remaining_tickets=request.POST.get('remaining_tickets')
        )
        return redirect('flights-list')
    else:
        context = {'form': form}
        return render(request, 'flightapp/add_flight.html', context)