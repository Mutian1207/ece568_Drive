# Generated by Django 4.1.5 on 2023-01-25 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rides',
            fields=[
                ('ride_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dest_addr', models.CharField(max_length=200)),
                ('arr_date_time', models.DateTimeField()),
                ('party_num', models.PositiveSmallIntegerField()),
                ('sharable', models.BooleanField()),
                ('status', models.CharField(choices=[('op', 'open'), ('cf', 'confirmed'), ('cp', 'complete')], max_length=2)),
                ('other_reg', models.TextField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('user_pwd', models.CharField(max_length=30)),
                ('is_driver', models.BooleanField()),
                ('vehic_type', models.CharField(choices=[('su', 'suv'), ('mp', 'mpv'), ('sd', 'sedan')], max_length=2, null=True)),
                ('lice_plate_number', models.CharField(max_length=10, null=True)),
                ('max_pass_num', models.PositiveSmallIntegerField(null=True)),
                ('other_reg', models.TextField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sharers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_party_num', models.PositiveSmallIntegerField()),
                ('share_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share_ride', to='basicapp.rides')),
                ('sharer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sharers', to='basicapp.users')),
            ],
        ),
        migrations.AddField(
            model_name='rides',
            name='driver_acc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='basicapp.users'),
        ),
        migrations.AddField(
            model_name='rides',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='basicapp.users'),
        ),
    ]