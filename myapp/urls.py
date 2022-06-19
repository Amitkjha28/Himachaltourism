

from django.conf.urls.static import static
from django.urls import path

from Himachaltourism import settings
from myapp import views

urlpatterns = [
    #path('', views.myindex),
    path('', views.my_index,name='myhome'),
    path('city/',views.my_destination,name='mydestination'),
    path('districtinfo/<int:my_id>',views.my_district,name='mydistrict'),
    path('contact', views.my_contact,name='mycontact'),
    path('reach', views.my_reach,name='myreach'),
    path('hotel/<int:d_id>', views.my_hotel,name='myhotel'),
    path('districthotel',views.my_district_2,name='mydistrict2'),
    path('booking', views.my_hotel_booking,name='myhotelbook')


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





