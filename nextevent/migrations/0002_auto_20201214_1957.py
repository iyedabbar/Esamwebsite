# Generated by Django 3.1.3 on 2020-12-14 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nextevent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nextevent',
            old_name='eventdate',
            new_name='eventdate1',
        ),
        migrations.RenameField(
            model_name='nextevent',
            old_name='eventname',
            new_name='eventname1',
        ),
        migrations.RenameField(
            model_name='nextevent',
            old_name='eventtime',
            new_name='eventtime1',
        ),
        migrations.RenameField(
            model_name='nextevent',
            old_name='thumnail',
            new_name='thumnail1',
        ),
    ]
