# Generated by Django 5.0.7 on 2024-08-16 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='task',
        ),
    ]
