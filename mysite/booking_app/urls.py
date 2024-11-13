from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'hotel', HotelListViewSet, basename='hotel_list')
router.register(r'room', RoomListViewSet, basename='room_list')
router.register(r'booking', BookingViewSet, basename='booking_list')
router.register(r'review', ReviewViewSet, basename='review_list')
router.register(r'hotel_image', HotelImageViewSet, basename='hotel-image_list')
router.register(r'room_image', RoomImageViewSet, basename='room-image_list')
router.register(r'hotel-detail', HotelDetailViewSet, basename='hotel_detail')
router.register(r'room-detail', RoomDetailViewSet, basename='room_detail')

urlpatterns = [
    path('', include(router.urls))
]
