# Generated by Django 3.1.3 on 2020-12-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_event_video_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='video_display',
            field=models.BooleanField(),
        ),
    ]
