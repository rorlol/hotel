from rest_framework import serializers
from .models import UserProfile,Country,City,Service,Hotel,ImageHotel,Room,ImageRoom,Review,BookingHotel


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class ImageHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageHotel
        fields = '__all__'

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model =Room
        fields = '__all__'

class ImageRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model =ImageRoom
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields = '__all__'

class BookingHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model =BookingHotel
        fields = '__all__'
