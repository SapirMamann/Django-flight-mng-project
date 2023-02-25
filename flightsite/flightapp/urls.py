from django.urls import path
from .views import *



urlpatterns = [
    path('flights/',                 GetAllFlights.as_view(), name="get_all_flights"),
    path('flights/<int:flight_id>/', GetFlightByID.as_view(), name="get_flight_by_id"),
]
