# Generated by Django 4.1.5 on 2023-04-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_all_orders_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_orders',
            name='delivery_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='all_orders',
            name='shipping_status',
            field=models.CharField(default='Pending Dispatch', max_length=50),
        ),
    ]