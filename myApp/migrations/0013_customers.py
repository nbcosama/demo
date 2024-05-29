# Generated by Django 4.1.5 on 2023-06-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_class_fee_for_month_class_total_fee_person2_num_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('customer_type', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('product', models.CharField(default='', max_length=30)),
                ('previous_amount', models.CharField(default='', max_length=30)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
