# Generated by Django 4.1.5 on 2023-06-22 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0022_payments_fee_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('fee_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remaining_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('fee_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.feestructure')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('payment_mode', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.invoice')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.student')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.student'),
        ),
    ]