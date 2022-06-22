from django.contrib import admin

# Register your models here.
from myapp.models import District, Hotel, Booking


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['district_name','district_info','district_reach','district_things']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['district','hotel_name','hotel_Image','price','discount_percent']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','check_in','check_out','room','adult','child']