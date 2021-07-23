from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import HotelSerializer, RoomTypeSerializer, StatusCalalogSerializer, GuestSerializer, RoomSerializer, ReservationSerializer
from api.models import Hotel, Room, RoomType, Guest, Reservation, ReservationStatusCalalog, ReservationStatusEvent, RoomReserved, InvoiceGuest


def index(request):
    """ Render index html for get data from API """
    return render(request, 'index.html',)


class HotelViewSet(viewsets.ModelViewSet):
    """API endpoint that allows get hotels."""
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows get room types."""
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    ordering = ['id']


class StatusCalalogViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows get catalog's status. """
    queryset = ReservationStatusCalalog.objects.all()
    serializer_class = StatusCalalogSerializer
    ordering = ['id']


class GuestViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows get Guest. """
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    ordering = ['id']


class RoomViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows get rooms. """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows get Reservations. """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
