# Generated by Django 3.2 on 2021-05-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production', models.CharField(max_length=100)),
                ('performance_date', models.TextField(blank=True)),
                ('location', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('posting_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
