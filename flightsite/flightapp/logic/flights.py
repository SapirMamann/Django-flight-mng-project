from ..models import Flight

class FlightsLogic:

    def get_all():
    
        all_flights = Flight.objects.all()
        return all_flights


    def get_by_id(id: int):
        flight = Flight.objects.get(id=flight.id).first()

        return flight