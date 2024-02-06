# Generated by Django 4.2.1 on 2023-06-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0002_doctor_tbl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_tbl',
            name='doctor_id_proof',
        ),
        migrations.AddField(
            model_name='doctor_tbl',
            name='DateOfJoining',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='doctor_tbl',
            name='doctor_NameOfProof',
            field=models.FileField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='doctor_tbl',
            name='doctor_qualification',
            field=models.DateField(null=True),
        ),
    ]