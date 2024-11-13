from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class HotelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'created_date']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel = HotelImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    owner = UserProfileSimpleSerializer()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'description', 'city', 'hotel', 'address', 'hotel_video',
                  'average_rating', 'stars', 'reviews', 'owner', 'created_date']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_price', 'room_type', 'room_status', 'all_inclusive']


class RoomDetailSerializer(serializers.ModelSerializer):
    room = RoomImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'hotel_room', 'room_price', 'room', 'room_type',
                  'room_status', 'reviews', 'room_description', 'all_inclusive']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
