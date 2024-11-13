from django_filters.rest_framework import FilterSet
from .models import Hotel, Room


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'stars': ['exact'],
            'country': ['exact'],
            'city': ['exact'],
        }


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_number': ['exact'],
            'hotel_room': ['exact'],
            'room_type': ['exact'],
            'room_status': ['exact'],
            'all_inclusive': ['exact'],
            'room_price': ['gt', 'lt'],
        }
