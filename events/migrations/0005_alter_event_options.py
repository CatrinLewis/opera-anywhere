# Generated by Django 3.2 on 2021-06-08 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['performance_date']},
        ),
    ]
