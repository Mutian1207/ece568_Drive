# Generated by Django 4.1.6 on 2023-02-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0007_merge_20230130_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='other_reg',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='other_reg',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]