# Generated by Django 4.1.5 on 2023-06-13 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='Fee_for_month',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='class',
            name='total_fee',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='person2',
            name='depr_name',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.department'),
        ),
    ]
