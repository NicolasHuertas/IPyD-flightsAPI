from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from flights import views

router = routers.DefaultRouter()
router.register(r'flights', views.FlightViewSet, 'flights')
router.register(r'reservations', views.ReservationViewSet, 'reservations')

urlpatterns = [
    path('api/', include(router.urls))
]