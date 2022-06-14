from django.contrib import admin

# Register your models here.
from myapp.models import District, Hotel


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['district_name','district_info','district_reach','district_things']

@admin.register(Hotel)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['district','hotel_name','hotel_Image','price','discount_percent']