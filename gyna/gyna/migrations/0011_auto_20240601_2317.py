# Generated by Django 3.0.14 on 2024-06-02 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0010_remove_request_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='mechanic',
            name='profile_pic',
        ),
    ]