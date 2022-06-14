# Generated by Django 4.0.5 on 2022-06-13 20:34

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=60)),
                ('district_Image', models.ImageField(upload_to='districtpics')),
                ('district_info', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('district_reach', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('district_things', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_Image', models.ImageField(upload_to='hotelpics')),
                ('price', models.IntegerField()),
                ('discount_percent', models.IntegerField(default=0)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.district')),
            ],
        ),
    ]
