from rest_framework import serializers
from .models import UserProfile,Country,City,Service,Hotel,ImageHotel,Room,ImageRoom,Review,BookingHotel


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username']

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '?'

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields = '__all__'

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model =Room
        fields = '__all__'

class ImageHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageHotel
        fields = '__all__'

class HotelListSerializers(serializers.ModelSerializer):
    country = CountrySerializers()
    city = CitySerializers()

    class Meta:
        model = Hotel
        fields = ['id','hotel_image','hotel_name','country','city']

class HotelDetailSerializers(serializers.ModelSerializer):
    country = CountrySerializers()
    city = CitySerializers()
    service = ServiceSerializers(many=True, read_only=True)
    owner = UserProfileSerializers()
    images_hotel = ImageHotelSerializers(read_only=True,many=True)
    room = RoomSerializers(read_only=True,many=True)
    review = ReviewSerializers(read_only=True,many=True)

    class Meta:
        model = Hotel
        fields = ['id','hotel_image','hotel_name','country','city','owner','service','images_hotel','room','review']

class ImageRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model =ImageRoom
        fields = '__all__'

class BookingHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model =BookingHotel
        fields = '__all__'
