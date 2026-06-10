from .views import (UserProfileViewSet,CountryViewSet,CityViewSet,ServiceViewSet,HotelListViewSet,HotelDetailViewSet,
                    ImageHotelViewSet,RoomViewSet,ImageRoomViewSet,ReviewViewSet,BookingHotelViewSet)
from rest_framework import routers
from django.urls import path,include


router = routers.DefaultRouter()


router.register(r'user_profile',UserProfileViewSet,basename='user_profile')
router.register(r'country',CountryViewSet,basename='country')
router.register(r'city',CityViewSet,basename='city')
router.register(r'service',ServiceViewSet,basename='service')
#router.register(r'hotel',HotelViewSet,basename='hotel')
router.register(r'image_hotel',ImageHotelViewSet,basename='image_hotel')
router.register(r'room',RoomViewSet,basename='room')
router.register(r'image_room',ImageRoomViewSet,basename='image_room')
router.register(r'review',ReviewViewSet,basename='review')
router.register(r'booking_hotel',BookingHotelViewSet,basename='booking_hotel')



urlpatterns = [
    path('', include(router.urls)),

    path('hotel/', HotelListViewSet.as_view(), name='hotel_list'),
    path('hotel/<int:pk>', HotelDetailViewSet.as_view(), name='hotel_detail')
]