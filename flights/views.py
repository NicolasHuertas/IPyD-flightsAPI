from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from .serializers import FlightSerializer, ReservationSerializer
from .models import Flight, Reservation

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params
        filter_kwargs = {param: value for param, value in query_params.items() if hasattr(Flight, param)}
        return queryset.filter(**filter_kwargs)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        flight_number = self.request.data.get('flight_number')
        seat_number = self.request.data.get('seat_number')
        existing_reservation = Reservation.objects.filter(flight_number=flight_number, seat_number=seat_number, cancelled=False).exists()
        flight_exists = Flight.objects.filter(flight_number=flight_number).exists()

        if not flight_exists:
            raise ValidationError({"error": "Flight not found."})
        elif existing_reservation:
            raise ValidationError({"error": "This seat is already booked."})
        else:
            serializer.save()
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        reservation = Reservation.objects.get(pk=pk)
        reservation.cancelled = True
        reservation.save()
        return Response({"message": "Reservation cancelled."}, status=status.HTTP_200_OK)