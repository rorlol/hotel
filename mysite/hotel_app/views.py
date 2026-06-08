from rest_framework import viewsets
from .models import UserProfile,Country,City,Service,Hotel,ImageHotel,Room,ImageRoom,Review,BookingHotel
from .serializers import (UserProfileSerializers,CountrySerializers,CitySerializers,ServiceSerializers,
                          HotelSerializers,ImageHotelSerializers,RoomSerializers,ImageRoomSerializers,
                          ReviewSerializers,BookingHotelSerializers)



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

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

class ImageHotelViewSet(viewsets.ModelViewSet):
    queryset = ImageHotel.objects.all()
    serializer_class = ImageHotelSerializers

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

class ImageRoomViewSet(viewsets.ModelViewSet):
    queryset = ImageRoom.objects.all()
    serializer_class = ImageRoomSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class BookingHotelViewSet(viewsets.ModelViewSet):
    queryset = BookingHotel.objects.all()
    serializer_class = BookingHotelSerializers

