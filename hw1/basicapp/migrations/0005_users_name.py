# Generated by Django 4.1.5 on 2023-01-28 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0004_alter_rides_driver_acc_alter_rides_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
