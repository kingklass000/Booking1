from django.contrib import admin
from .models import *


class HotelImageInlines(admin.TabularInline):
    model = HotelImage
    extra = 1


class RoomImageInlines(admin.TabularInline):
    model = RoomImage
    extra = 1


class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageInlines]


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInlines]


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Booking)
