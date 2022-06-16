from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import District


def my_index(request):
    return render(request,"tourism.html")

def my_destination(request):
    district_data = District.objects.all()
    return  render(request,"Destination.html",{ 'districtdata' :district_data})

def my_district(request,my_id):
    district_data = District.objects.get(id=my_id)
    return  render(request,"district.html",{ 'districtdata' :district_data})