# Generated by Django 4.1.5 on 2023-07-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0058_remove_workoutlist_tbl_excname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutlist_tbl',
            name='month',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
