# Generated by Django 4.1.5 on 2023-07-23 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0057_rename_member_feedback_tbl_memberid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutlist_tbl',
            name='excname',
        ),
        migrations.RemoveField(
            model_name='workoutlist_tbl',
            name='reps',
        ),
        migrations.RemoveField(
            model_name='workoutlist_tbl',
            name='sets',
        ),
        migrations.AddField(
            model_name='workoutlist_tbl',
            name='trainer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.trainer_tbl'),
        ),
        migrations.CreateModel(
            name='Exercise_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excname', models.CharField(max_length=100, null=True)),
                ('reps', models.IntegerField(null=True)),
                ('work_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitapp.workoutlist_tbl')),
            ],
        ),
    ]
