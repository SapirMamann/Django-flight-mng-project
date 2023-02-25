from ..logic.flights import FlightsLogic

from rest_framework.views import APIView, Response


def get_all_flights():

    try:
        all_flights = FlightsLogic.get_all()

        return all_flights
    except Exception as e:
        return Response(str(e))
