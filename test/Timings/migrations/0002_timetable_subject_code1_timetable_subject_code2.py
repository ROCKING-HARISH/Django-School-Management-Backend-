# Generated by Django 4.1.7 on 2023-02-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='subject_code1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='subject_code2',
            field=models.CharField(blank=True, default='NA', max_length=50, null=True),
        ),
    ]
