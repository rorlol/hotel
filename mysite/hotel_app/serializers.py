from rest_framework import serializers
from .models import UserProfile,Country,City,Service,Hotel,ImageHotel,Room,ImageRoom,Review,BookingHotel
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username']

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields = ['id','user','comment']

class ImageRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model =ImageRoom
        fields = '__all__'

class RoomSerializers(serializers.ModelSerializer):
    room_images = ImageRoomSerializers(read_only=True,many=True)
    class Meta:
        model =Room
        fields = ['id','room_image','room_number','price','room_type','room_status','room_images']

class ImageHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageHotel
        fields = '__all__'

class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','city_name']

class HotelSimpleSerializers(serializers.ModelSerializer):
    country = CountrySerializers()

    class Meta:
        model = Hotel
        fields = ['id','hotel_image','hotel_name','country']

class HotelListSerializers(serializers.ModelSerializer):
    country = CountrySerializers()
    city = CityListSerializers()
    get_avg_rating = serializers.SerializerMethodField()
    get_count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id','hotel_image','hotel_name','country','city','get_avg_rating','get_count_rating']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def get_count_rating(self,obj):
        return obj.get_count_rating()

class CityDetailSerializers(serializers.ModelSerializer):
    hotel = HotelSimpleSerializers(read_only=True,many=True)

    class Meta:
        model = City
        fields = ['id','city_name','hotel']

class HotelDetailSerializers(serializers.ModelSerializer):
    country = CountrySerializers()
    city = CityListSerializers()
    service = ServiceSerializers(many=True, read_only=True)
    owner = UserProfileSerializers()
    images_hotel = ImageHotelSerializers(read_only=True,many=True)
    room = RoomSerializers(read_only=True,many=True)
    reviews = ReviewSerializers(read_only=True,many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id','hotel_image','hotel_name','country','city','owner','service','images_hotel','room','reviews',
                  'get_avg_rating','get_count_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()

class BookingHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model =BookingHotel
        fields = '__all__'
