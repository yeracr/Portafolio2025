# Generated by Django 5.0.7 on 2024-08-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0018_alter_request_vehicle_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='vehicle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
