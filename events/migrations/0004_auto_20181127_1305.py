# Generated by Django 2.1.2 on 2018-11-27 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_host_grad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='host_grad',
            new_name='grad',
        ),
    ]
