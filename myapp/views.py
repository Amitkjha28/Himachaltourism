import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import District, Hotel, Booking


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
    hotelid = request.GET.get("hotelid")
    districtid = request.GET.get("distid")
    room_available = Hotel.objects.filter(id= hotelid,district=districtid)
    return  render(request,"room_availability.html",{ 'availabledata' :room_available})

def my_room_booking(request):
    bookingobj = Booking()
    check_in = request.POST.get("date1")
    check_out = request.POST.get("date2")
    adult = request.POST.get("adult")
    child = request.POST.get("child")
    room = request.POST.get("room")
    bookingobj.check_in = check_in
    bookingobj.check_out = check_out
    bookingobj.adult = adult
    bookingobj.child = child
    bookingobj.room = room
    bookingobj.save()
    booking_no = Booking.objects.latest('id')
    return render(request, "booking.html", {'check_in':check_in,'check_out':check_out,'adult':adult,'child':child,'room':room,'booking_no':booking_no})