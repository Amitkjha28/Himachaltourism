import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import District, Hotel


def my_index(request):
    current_date = datetime.datetime.now()
    return render(request,"tourism.html",{ 'current_datetime' :current_date})

def my_destination(request):
    district_data = District.objects.all()
    return  render(request,"Destination.html",{ 'districtdata' :district_data})

def my_district(request,my_id):
    district_data = District.objects.get(id=my_id)
    return  render(request,"district.html",{ 'districtdata' :district_data})

def my_contact(request):
    return  render(request,"contact.html")

def my_reach(request):
    return  render(request,"how_to_reach.html")

def my_district_2(request):
    district_data = District.objects.all()
    return  render(request,"district-2.html",{ 'districtdata' :district_data})

def my_hotel(request,d_id):
    hotel_data = Hotel.objects.filter(district=d_id)
    return  render(request,"hotel.html",{ 'hoteldata' :hotel_data})

def my_room_availability(request):
    room_available = Hotel.objects.all()
    return  render(request,"room_availability.html",{ 'availabilitydata' :room_available})

def my_room_booking(request):
    hotel_booking = Hotel.objects.all()
    return  render(request,"booking.html",{ 'bookingdata' :hotel_booking})