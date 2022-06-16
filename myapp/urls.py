

from django.conf.urls.static import static
from django.urls import path

from Himachaltourism import settings
from myapp import views

urlpatterns = [
    #path('', views.myindex),
    path('', views.my_index,name='myhome'),
    path('city',views.my_destination,name='mydestination'),
    path('districtinfo',views.my_district,name='mydistrict'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





