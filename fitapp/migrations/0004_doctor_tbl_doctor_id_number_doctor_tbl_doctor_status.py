# Generated by Django 4.2.1 on 2023-06-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0003_remove_doctor_tbl_doctor_id_proof_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_tbl',
            name='doctor_ID_Number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='doctor_tbl',
            name='doctor_Status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
