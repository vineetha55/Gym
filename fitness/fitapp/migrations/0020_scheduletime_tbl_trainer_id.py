# Generated by Django 4.2.1 on 2023-06-28 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0019_remove_scheduletime_tbl_membername'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduletime_tbl',
            name='trainer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.trainer_tbl'),
        ),
    ]
