# Generated by Django 4.1.5 on 2023-06-08 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_department_person2_depr_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person2',
            name='depr_name',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]