# Generated by Django 4.2.1 on 2023-06-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0016_assigntrainer_tbl'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberregistration_tbl',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
