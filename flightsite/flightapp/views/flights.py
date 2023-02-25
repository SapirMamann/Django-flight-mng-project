from ..serializers.flight_serializer import FlightSerializer
from ..logic.flights import FlightsLogic

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class GetAllFlights(APIView):
    serializer_class = FlightSerializer       


    def get(self, request):

        try:
            all_flights = FlightsLogic.get_all(request)
            serializer = self.serializer_class(all_flights, many=True)
            
            return Response(serializer.data, status=200)

        except Exception as e:
            # Or pass to a Exception factory function
            # that will return a custom object
            return Response(str(e))


class GetFlightByID(APIView):
    serializer_class = FlightSerializer       


    def get(self, request, flight_id: int):

        try:
            flight = FlightsLogic.get_by_id(request, flight_id)
            serializer = self.serializer_class(flight)
            return Response(serializer.data, status=200)

        except Exception as e:
            # Or pass to a Exception factory function
            # that will return a custom object
            return Response(str(e))
