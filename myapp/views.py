from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myindex(request):
    return render(request,"tourism.html")