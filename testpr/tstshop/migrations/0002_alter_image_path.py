# Generated by Django 4.1.4 on 2022-12-16 18:19

from django.db import migrations
import tstshop.fields
import tstshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('tstshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=tstshop.fields.WEBPField(upload_to=tstshop.models.image_folder, verbose_name='path'),
        ),
    ]