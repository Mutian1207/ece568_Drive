# Generated by Django 4.1.5 on 2023-01-29 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0005_users_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
