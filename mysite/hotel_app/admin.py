from django.contrib import admin
from .models import UserProfile,Country,City,Service,Hotel,ImageHotel,Room,ImageRoom,Review,BookingHotel

class ImageHotelInline(admin.TabularInline):
    model = ImageHotel
    extra = 1

class ImageRoomInline(admin.TabularInline):
    model = ImageRoom
    extra = 1

class Admin(admin.ModelAdmin):
    inlines = [ImageHotelInline,ImageRoomInline]


admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Service)
admin.site.register(Hotel)
#admin.site.register(ImageHotel)
admin.site.register(Room)
#admin.site.register(ImageRoom)
admin.site.register(Review)
admin.site.register(BookingHotel)