# Generated by Django 4.1.5 on 2023-06-13 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_class_fee_for_month_class_total_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person2',
            name='num_name',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.class'),
        ),
    ]