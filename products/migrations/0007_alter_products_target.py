# Generated by Django 4.1.5 on 2023-03-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='target',
            field=models.CharField(max_length=20),
        ),
    ]
