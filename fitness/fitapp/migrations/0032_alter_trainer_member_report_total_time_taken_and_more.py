# Generated by Django 4.1.5 on 2023-07-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0031_workout_details_trainer_member_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer_member_report',
            name='Total_Time_Taken',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='workout_details',
            name='Total_Time_Taken',
            field=models.IntegerField(null=True),
        ),
    ]
