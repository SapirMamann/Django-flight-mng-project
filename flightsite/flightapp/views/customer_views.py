from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from flightapp.forms import MyUserCreationForm, TicketCreationForm
from flightapp.models import User, Ticket, Flight, Customer

def cust_index(request):
    """
    Customer's home page
    """
    return render(request, 'flightapp/customer_index.html')


def login_page(request):
    page = 'login'

    # if request.user.is_authenticated:  #a logged in user cant manually go to login page.
    #     return redirect('cust-index')
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")
        
        user = authenticate(request, email=email, password=password)  #user authentication, he exists
        
        if user is not None:  #we got a user -> log him in
            login(request, user)
            return redirect('cust-index')
        else:
            messages.error(request, 'Username OR Password does not exist')
            
    context = {'page': page}
    return render(request, 'flightapp/login_register.html', context)


def register_page(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            """
            needs to be modified
            """
            # user = form.save(commit=False)
            # user.username = user.username.lower()
            # user.save()

            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            pass
            return redirect('cust-index')
        else: 
            messages.error(request, 'An error occured during registration')
 
    context = {'form': form}                            #Show the registration form
    return render(request, 'flightapp/login_register.html', context)


def logout_page(request):
    """
    logout the user
    """
    logout(request)
    return redirect('anonymous-index')


def user_tickets(request):
    """
    Show all the tickets of a user
    """
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'flightapp/user_tickets.html', context)


def add_tickets(request):
    """
    When a user wants to buy a ticket to a flight
    """
    form = TicketCreationForm()

    if request.method == 'POST':
        flight_no = Flight.objects.get(id=request.POST.get('flight_no'))
        customer = Customer.objects.get(id=request.POST.get('customer'))

        new_ticket = Ticket.objects.create(
            flight_no=flight_no,
            customer=customer
        )
        return redirect('user_tickets')
    
    flights_list = Flight.objects.all()                         #kinda shitty but later ill use react anyway. Showing all flights available
    context = {'form': form, 'flights_list': flights_list}
    return render(request, 'flightapp/add_ticket.html', context)












    # if request.user.is_authenticated:
    #     return redirect('cust-index')
    
    # if request.method == 'POST':
    #     flight_id = request.POST.get('flight_id')
    #     ticket_price = request.POST.get('ticket_price')
        
    #     try:
    #         flight = User.objects.get(id=flight_id)
    #     except:
    #         messages.error(request, "Flight does not exist")
        
    #     try:
    #         ticket = User.objects.get(id=ticket_price)
    #     except:
    #         messages.error(request, "Ticket price does not exist")
        
    #     if flight is not None and ticket is not None:
    #         flight.tickets.add(ticket)
    #         flight.save()
    #         messages.success(request, "Ticket added successfully")
    #         return redirect('cust-index')
    #     else:
    #         messages.error(request, "Flight or Ticket price does not exist")
    # else: