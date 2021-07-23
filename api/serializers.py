from rest_framework import serializers
from .models import Hotel, Room, RoomType, Guest, Reservation, ReservationStatusCalalog, ReservationStatusEvent, RoomReserved, InvoiceGuest


class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'description', 'is_active', ]


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'type_name']


class StatusCalalogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReservationStatusCalalog
        fields = ['id', 'name']


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'details']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_name', 'description', 'room_type', 'current_price', 'is_active', ]


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'date_start', 'date_end', 'created_at',
                  'updated_at', 'total_price', 'invoices', 'rooms', 'status']

