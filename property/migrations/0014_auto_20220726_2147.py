# Generated by Django 2.2.24 on 2022-07-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats_have',
            field=models.ManyToManyField(related_name='flat_owner', to='property.Flat'),
        ),
    ]
