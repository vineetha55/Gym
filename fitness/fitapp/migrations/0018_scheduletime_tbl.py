# Generated by Django 4.2.1 on 2023-06-28 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0017_memberregistration_tbl_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleTime_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=20, null=True)),
                ('StarTime', models.TimeField(auto_now_add=True, null=True)),
                ('EndTime', models.TimeField(auto_now_add=True, null=True)),
                ('memberassigned', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.assigntrainer_tbl')),
            ],
        ),
    ]
