# Generated by Django 4.2.1 on 2023-06-15 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0007_package_tbl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package_tbl',
            name='package_name',
        ),
    ]