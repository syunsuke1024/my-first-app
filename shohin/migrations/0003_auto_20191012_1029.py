# Generated by Django 2.1.7 on 2019-10-12 01:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shohin', '0002_shohin_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shohin',
            name='photo',
        ),
        migrations.AddField(
            model_name='shohin',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
