# Generated by Django 4.2.1 on 2023-07-19 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0041_doctor_leave_dates_tbl_doctor_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer_tbl',
            name='trainer_Salary',
            field=models.IntegerField(null=True),
        ),
    ]
