# Generated by Django 2.2.24 on 2022-07-21 14:23

from django.db import migrations


def update_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        flat.new_building = flat.construction_year >= 2015
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220721_1710'),
    ]

    operations = [
        migrations.RunPython(update_new_building),
    ]
