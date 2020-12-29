# Generated by Django 3.1.3 on 2020-12-28 12:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_display',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
    ]