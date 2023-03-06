from .base_facade import BaseFacade
# from flightapp.models import AirlineCompany


class AirlineFacade(BaseFacade):
    def __init__(self):
        super().__init__()
        

    def login(self):
        pass

    def register(self):
        pass



    def get_all_airlines(self):
        return super().get_all_airlines()

    def get_airline_by_id(self):
        pass

    def get_airline_by_parameters(self):
        pass


   
    def get_all_flights(self):
        pass

    def get_flight_by_id(self):
        pass

    def get_flight_by_parameters(self):
        pass



    def get_all_countries(self):
        pass

    def get_country_by_id(self):
        pass



    def get_my_flights(self):
        pass