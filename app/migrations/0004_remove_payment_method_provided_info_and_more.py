# Generated by Django 4.1.2 on 2023-09-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_payment_method_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_method',
            name='provided_info',
        ),
        migrations.AlterField(
            model_name='payment_method',
            name='btc_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='payment_method',
            name='payoneer_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='payment_method',
            name='paypal_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='payment_method',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=50),
        ),
    ]
