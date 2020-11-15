# Generated by Django 3.1 on 2020-11-04 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_remove_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='thumnail',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.event')),
            ],
        ),
    ]
