# Generated by Django 4.2.2 on 2023-12-12 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0028_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.student'),
        ),
    ]
