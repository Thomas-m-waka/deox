# Generated by Django 4.1.5 on 2023-04-07 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_remove_orderitems_order_orderitems_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='order_id',
            field=models.ForeignKey(default=80, on_delete=django.db.models.deletion.CASCADE, to='products.orderitems'),
        ),
    ]
