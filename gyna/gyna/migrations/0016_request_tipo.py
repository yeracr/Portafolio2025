# Generated by Django 5.0.7 on 2024-08-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0015_remove_attendance_mechanic_remove_customer_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='tipo',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
