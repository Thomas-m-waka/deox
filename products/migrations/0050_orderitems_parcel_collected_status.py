# Generated by Django 4.1.5 on 2023-04-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0049_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='parcel_collected_status',
            field=models.BooleanField(default=False),
        ),
    ]