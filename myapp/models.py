from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class District(models.Model):
    district_name = models.CharField(max_length=60)
    district_Image = models.ImageField(upload_to='districtpics')
    district_info = RichTextUploadingField(null=True, blank=True)
    district_reach = RichTextUploadingField(null=True, blank=True)
    district_things= RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.district_name

class Hotel(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    hotel_Image = models.ImageField(upload_to='hotelpics')
    price = models.IntegerField()
    discount_percent = models.IntegerField(default=0)

    def __str__(self):
        return self.hotel_name
