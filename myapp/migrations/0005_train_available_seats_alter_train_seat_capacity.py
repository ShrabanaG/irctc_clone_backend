# Generated by Django 4.2.14 on 2024-07-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_arrival_time_at_departure_train_arrival_time_at_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='available_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='train',
            name='seat_capacity',
            field=models.IntegerField(),
        ),
    ]
