# Generated by Django 4.1.7 on 2023-02-26 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timings', '0002_timetable_subject_code1_timetable_subject_code2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='subject_code1',
            new_name='code1',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='subject_code2',
            new_name='code2',
        ),
    ]