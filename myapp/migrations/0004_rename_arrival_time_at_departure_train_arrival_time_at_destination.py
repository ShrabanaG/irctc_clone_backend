# Generated by Django 4.2.14 on 2024-07-24 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_train'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='arrival_time_at_departure',
            new_name='arrival_time_at_destination',
        ),
    ]
