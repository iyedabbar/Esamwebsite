# Generated by Django 3.1.2 on 2020-10-29 22:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
