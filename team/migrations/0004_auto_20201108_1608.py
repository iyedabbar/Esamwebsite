# Generated by Django 3.1 on 2020-11-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20201108_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='message_testimonial',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='testimonial',
            field=models.BooleanField(),
        ),
    ]
