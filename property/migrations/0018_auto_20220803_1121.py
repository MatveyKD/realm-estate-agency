# Generated by Django 2.2.24 on 2022-08-03 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20220730_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints', to='property.Flat', verbose_name='Квартира, на которую написали жалобу'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='writed_complaints', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, написавший жалобу'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats_have',
            field=models.ManyToManyField(related_name='owners', to='property.Flat'),
        ),
    ]