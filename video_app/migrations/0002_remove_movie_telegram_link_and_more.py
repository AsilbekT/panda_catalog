# Generated by Django 4.2.4 on 2024-01-16 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='telegram_link',
        ),
        migrations.RemoveField(
            model_name='series',
            name='telegram_link',
        ),
    ]