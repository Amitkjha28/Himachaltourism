from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import District


def my_index(request):
    return render(request,"tourism.html")

def my_destination(request):
    district_data = District.objects.all()
    return  render(request,"Destination.html",{ 'districtdata' :district_data})