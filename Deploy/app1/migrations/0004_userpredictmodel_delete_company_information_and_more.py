# Generated by Django 4.0.3 on 2023-08-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_company_information_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPredictModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Air_temperature_K', models.CharField(max_length=100)),
                ('Process_temperature_K', models.CharField(max_length=100)),
                ('Rotational_speed_rpm', models.CharField(max_length=100)),
                ('Torque_Nm', models.CharField(max_length=100)),
                ('Tool_wear_min', models.CharField(max_length=100)),
                ('Failure_Type', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Company_Information',
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
        migrations.DeleteModel(
            name='Machine_Type',
        ),
    ]
