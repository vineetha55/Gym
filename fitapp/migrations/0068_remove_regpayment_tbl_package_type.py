# Generated by Django 4.2.1 on 2023-08-05 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0067_remove_package_tbl_advanceamount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regpayment_tbl',
            name='package_type',
        ),
    ]
