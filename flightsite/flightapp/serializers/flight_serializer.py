from rest_framework import serializers
from ..models import Flight

  
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight

        # Which fields should be included in the parsed data?
        # Perhaps you would like to exclude some fields?
        fields = (
            'airline_company',
            'destination_country',
            'origin_country',
            'departure_time',
            'landing_time',
            'remaining_tickets',
        )