# Generated by Django 4.0.5 on 2022-06-19 17:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_district_district_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='contact',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
