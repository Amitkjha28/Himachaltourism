# Generated by Django 4.0.5 on 2022-06-22 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='hotel_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
