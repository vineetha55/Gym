# Generated by Django 4.2.1 on 2023-07-22 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0055_rename_name_feedback_tbl_full_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback_tbl',
            old_name='full',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='feedback_tbl',
            old_name='memberid',
            new_name='member',
        ),
    ]
