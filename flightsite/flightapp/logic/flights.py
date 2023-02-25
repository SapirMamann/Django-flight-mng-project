from ..models import Flight

class FlightsLogic:

    def get_all(request):

        all_flights = Flight.objects.all()

        if all_flights.count() == 0:
            raise Exception('No flights found in db!')

        return all_flights


    def get_by_id(request, flight_id: int):

        flight = Flight.objects.get(id=flight_id)

        if flight == None:
            raise Exception('Flight not found!')

        return flight
