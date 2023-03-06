from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from flightapp.models import Country, User, AirlineCompany
from flightapp.forms import MyUserCreationForm, CustomerForm, AirlineCreationForm, UserCreationForm
from flightapp.dal.admin_dal import Admin


def admin_index(request):
    """
    Home Page of an admin
    """
    return render(request, 'flightapp/admin_index.html')


def customers_list(request):
    """
    Show all customers 
    """
    context = {'cust_list': Admin.get_all_customers}
    return render(request, 'flightapp/cust_list.html', context)


def add_user(request):
    pass
#     form = MyUserCreationForm()

#     if request.method == "POST":
#         form = MyUserCreationForm(request.POST)
#         if form.is_valid():
#             # user = authenticate(request, email='.com', password='password')
#             user = form.save(commit=False)
#             user.save()
#             # return redirect('admin-index')
#             return HttpResponse('yes')
#         else:
#             return HttpResponse('no no')
    
#     context= {'form': form}
#     return render(request, 'flightapp/user_form.html', context)
        
# def register_page(request):
#     pass
#     form = CustomerForm()

# #     if request.method == "POST":
# #         # user = 'sapir'
# #         pass

# #     else:
#     context= {'form': form}
#     return render(request, 'flightapp/login_register.html', context)



    # form = MyUserCreationForm()
    
    # if request.method == 'POST':
    #     form = MyUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username.lower()
    #         user.save()
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'An error occured during registration')
        
#here i would call the dal.py functions and return responses
#functions with try except. 


# @login_required
def add_airline(request):
    """
    Adding an airline company. 
    Only an admin can add airline companies.
    """
    form = AirlineCreationForm()
    countries = Country.objects.all()
    form = AirlineCreationForm()
    countries = Country.objects.all()

    if request.method == 'POST':                            
        username_id = request.POST.get('user')
        user = User.objects.get(id=username_id)
        country_id = request.POST.get('country')
        country, created = Country.objects.get_or_create(id=country_id)  #causing a problem while creating?

        AirlineCompany.objects.create(                          #creating the new instance (airline company) with all of its required fields
            user=user,
            name=request.POST.get('name'),
            country=country,
        )
        return redirect('airlines-list') #add alert that an airline company created
    else:                           #show the form 
        context = {'form': form, 'countries':countries}                         
        return render(request, 'flightapp/add_airline.html', context)

