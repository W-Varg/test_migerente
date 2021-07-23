from django.urls import path, include
from rest_framework import routers
from api.views import index,  HotelViewSet, RoomTypeViewSet, StatusCalalogViewSet, GuestViewSet, RoomViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'room_types', RoomTypeViewSet)
router.register(r'status_calalogs', StatusCalalogViewSet)
router.register(r'guests', GuestViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
