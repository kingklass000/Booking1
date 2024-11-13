from rest_framework import viewsets
from .serializer import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .filter import HotelFilter, RoomFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import (CheckOwner, CheckCRUD, CheckHotelOwner, CheckRoom, CheckBooking, CheckOwnerOfReview,
                          CheckHotelNumberOwner, CheckOwnerOfBooking, ReadOnlyForAll)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSimpleSerializer


class HotelListViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilter
    search_fields = ['hotel_name']
    ordering_fields = ['stars']
    permission_classes = [CheckCRUD]


class RoomListViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ['hotel_number']
    ordering_fields = ['room_price',]
    permission_classes = [CheckCRUD]


class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    permission_classes = [CheckCRUD, CheckOwner, CheckHotelOwner, CheckHotelNumberOwner]

    def perform_create(self, serializer):
        serializer.save(owmer=self.request.user)


class RoomDetailViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    permission_classes = [CheckCRUD, CheckRoom]


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
    permission_classes = [ReadOnlyForAll]


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer
    permission_classes = [ReadOnlyForAll]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [CheckBooking, CheckOwnerOfBooking]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CheckOwnerOfReview]
