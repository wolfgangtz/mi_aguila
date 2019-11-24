# Generated by Django 2.2.7 on 2019-11-24 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20191124_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='car_plate',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='trips', to='trips.City'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trips.Country'),
        ),
    ]