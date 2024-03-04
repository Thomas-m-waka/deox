# Generated by Django 4.1.5 on 2023-03-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('service_name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
    ]