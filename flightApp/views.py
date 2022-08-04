from django.shortcuts import render
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from flightApp.models import Flight, Passenger, Reservation
from rest_framework import viewsets


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
    
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


