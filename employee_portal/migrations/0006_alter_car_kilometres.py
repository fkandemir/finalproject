# Generated by Django 5.0.3 on 2024-03-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_portal', '0005_alter_car_doors_alter_car_engine_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='kilometres',
            field=models.IntegerField(),
        ),
    ]