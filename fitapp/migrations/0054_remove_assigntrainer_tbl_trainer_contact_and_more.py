# Generated by Django 4.2.1 on 2023-07-22 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0053_assigntrainer_tbl_trainer_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigntrainer_tbl',
            name='trainer_Contact',
        ),
        migrations.RemoveField(
            model_name='assigntrainer_tbl',
            name='trainer_Email',
        ),
        migrations.RemoveField(
            model_name='assigntrainer_tbl',
            name='trainer_Name',
        ),
    ]
