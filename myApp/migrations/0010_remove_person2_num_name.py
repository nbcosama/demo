# Generated by Django 4.1.5 on 2023-06-13 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_person2_num_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person2',
            name='num_name',
        ),
    ]
