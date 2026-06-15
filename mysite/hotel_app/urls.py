from .views import (UserProfileViewSet,CountryViewSet,CityListViewSet,CityDetailViewSet,ServiceViewSet,HotelListViewSet,HotelDetailViewSet,
                    ImageHotelViewSet,RoomViewSet,ImageRoomViewSet,ReviewViewSet,BookingHotelViewSet,RegisterView,CustomLoginView,LogoutView)
from rest_framework import routers
from django.urls import path,include


router = routers.DefaultRouter()


router.register(r'user_profile',UserProfileViewSet,basename='user_profile')
router.register(r'country',CountryViewSet,basename='country')
#router.register(r'city',CityViewSet,basename='city')
router.register(r'service',ServiceViewSet,basename='service')
#router.register(r'hotel',HotelViewSet,basename='hotel')
router.register(r'image_hotel',ImageHotelViewSet,basename='image_hotel')
router.register(r'room',RoomViewSet,basename='room')
router.register(r'image_room',ImageRoomViewSet,basename='image_room')
router.register(r'review',ReviewViewSet,basename='review')
router.register(r'booking_hotel',BookingHotelViewSet,basename='booking_hotel')



urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('hotel/', HotelListViewSet.as_view(), name='hotel_list'),
    path('hotel/<int:pk>', HotelDetailViewSet.as_view(), name='hotel_detail'),
    path('city/', CityListViewSet.as_view(), name='city_list'),
    path('city/<int:pk>', CityDetailViewSet.as_view(), name='city_detail'),
]