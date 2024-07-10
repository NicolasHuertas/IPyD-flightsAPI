from django.db import models

class Reservation(models.Model):
    flight_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cancelled = models.BooleanField(default=False)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.flight_number} - {self.seat_number}"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} to {self.arrival_city}"