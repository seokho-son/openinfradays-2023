# Generated by Django 4.2.2 on 2023-06-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='techsession',
            name='event_date',
            field=models.CharField(choices=[('Day 1', 'Day1'), ('Day 2', 'Day2')], default='Day 1', max_length=10),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='event_date',
            field=models.CharField(choices=[('Day 1', 'Day1'), ('Day 2', 'Day2')], default='Day 1', max_length=10),
        ),
    ]
