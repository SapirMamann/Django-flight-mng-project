from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('add_user/', views.add_user, name="add-user"),

    path('', views.anonymous_index, name="anonymous-index"),
    path('countries_list/', views.countries_list, name="countries-list"),  #probably not needed

    path('cust/', views.cust_index, name="cust-index"),
    path('user_tickets/', views.user_tickets, name="user-tickets"),
    path('add_ticket/', views.add_tickets, name="add-ticket"),

    path('airline/', views.airline_index, name="airline-index"),
    path('airline_register/', views.airline_register, name="airline-register"),  #dont know about it
    path('airline_detail/', views.airline_detail, name="airline-detail"),
    
    path('flights_list/', views.flights_list, name="flights-list"),
    path('add_flight/', views.add_flight, name="add-flight"),

    path('admin/', views.admin_index, name="admin-index"),
    path('cust_list/', views.customers_list, name="cust-list"),
    path('airlines_list/', views.airlines_list, name="airlines-list"),
    path('add_airline/', views.add_airline, name="add-airline"),


]
