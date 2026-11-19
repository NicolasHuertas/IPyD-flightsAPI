# IPyD Flights API

## Overview
The IPyD Flights API is a Django-based microservice that manages flight reservations and flight information. It provides endpoints to create, retrieve, and cancel flight seat reservations, as well as query available flights.

## Features
- Manage flight seat reservations
- Query available flights
- Cancel reservations
- RESTful API endpoints
- PostgreSQL database integration
- CORS support for cross-origin requests

## Technology Stack
- **Framework**: Django 4.2.6
- **API**: Django REST Framework 3.14.0
- **Database**: PostgreSQL (psycopg2)
- **Container**: Docker & Docker Compose

## Prerequisites
- Docker and Docker Compose
- Python 3.x (for local development)
- PostgreSQL (if running without Docker)

## Installation

### Using Docker (Recommended)
```bash
# Build and run the container
docker-compose up --build

# The service will be available at http://localhost:8000
```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver 0.0.0.0:8000
```

## API Endpoints

### Get All Flights
```
GET /api/flights/
```

### Get Single Flight
```
GET /api/flights/{id}/
```

### Get All Reservations
```
GET /api/reservations/
```

### Get Single Reservation
```
GET /api/reservations/{id}/
```

### Create Flight Reservation
```
POST /api/reservations/
Content-Type: application/json

{
  "flight_number": "AA123",
  "first_name": "John",
  "last_name": "Doe",
  "seat_number": "12A",
  "email": "john.doe@example.com",
  "phone": "1234567890"
}
```

### Cancel Reservation
```
DELETE /api/reservations/{id}/
```

## Environment Variables
Configure the following environment variables for database connection:
- `DATABASE_URL`: PostgreSQL connection string

## Docker Configuration
The service runs on port 8000 and can be deployed using the provided Dockerfile and docker-compose configuration.

## Related Services
This service is part of the IPyD (Integrated Python Booking System) ecosystem:
- **API Gateway**: Routes requests to all microservices
- **Orchestrator**: Coordinates combined flight and hotel reservations
- **Frontend**: React-based user interface

## License
ISC

## Author
Nicolas Huertas
