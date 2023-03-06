from abc import ABC, abstractmethod

from ..dal.airline_dal import AirlineDal
from flightapp.models import AirlineCompany

#logics, we get the input here 
#we call the dal here
#alll abstract because i only inherite from it

class BaseFacade(ABC):
    @abstractmethod
    def login(self):
        pass


    @abstractmethod
    def register(self):
        pass


    @abstractmethod
    def get_all_airlines(self):
        # airlines = AirlineCompany.objects.all()
        # return airlines
        dal = AirlineDal()
        airlines = dal.get_all_airlines()
        return airlines


    @abstractmethod
    def get_airline_by_id(self):
        pass


    @abstractmethod
    def get_airline_by_parameters(self):
        pass

   
    @abstractmethod
    def get_all_flights(self):
        pass


    @abstractmethod
    def get_flight_by_id(self):
        pass


    @abstractmethod
    def get_flight_by_parameters(self):
        pass



    @abstractmethod
    def get_all_countries(self):
        pass

    @abstractmethod
    def get_country_by_id(self):
        pass
