# Generated by Django 2.1.2 on 2018-11-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_remove_event_graduation'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='host_graduation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='graduation',
            field=models.CharField(default='', max_length=50),
        ),
    ]