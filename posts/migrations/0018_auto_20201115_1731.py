# Generated by Django 3.1.3 on 2020-11-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20201106_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='packages', to='posts.category'),
        ),
    ]