from rest_framework import viewsets,generics
from .models import UserProfile,Country,City,Service,Hotel,ImageHotel,Room,ImageRoom,Review,BookingHotel
from .serializers import (UserProfileSerializers,CountrySerializers,CitySerializers,ServiceSerializers,
                          HotelListSerializers,HotelDetailSerializers,ImageHotelSerializers,RoomSerializers,
                          ImageRoomSerializers,ReviewSerializers,BookingHotelSerializers)
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HotelFilter,RoomFilter
from .pagination import HotelPagination,RoomPagination


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers

class HotelListViewSet(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializers
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['hotel_name']
    filterset_class = HotelFilter
    pagination_class = HotelPagination

class HotelDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializers

class ImageHotelViewSet(viewsets.ModelViewSet):
    queryset = ImageHotel.objects.all()
    serializer_class = ImageHotelSerializers

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    filter_backends = [OrderingFilter,DjangoFilterBackend]
    ordering_fields = ['created_at']
    filterset_class = RoomFilter
    pagination_class = RoomPagination

class ImageRoomViewSet(viewsets.ModelViewSet):
    queryset = ImageRoom.objects.all()
    serializer_class = ImageRoomSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    filter_backends = [OrderingFilter]
    ordering_fields = ['rating']

class BookingHotelViewSet(viewsets.ModelViewSet):
    queryset = BookingHotel.objects.all()
    serializer_class = BookingHotelSerializers

