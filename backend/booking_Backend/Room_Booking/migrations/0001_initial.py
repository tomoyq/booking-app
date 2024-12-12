# Generated by Django 5.1.4 on 2024-12-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(choices=[('suitte', 'Suite'), ('standard', 'Standard Room'), ('deluxe', 'Deluxe Room')], max_length=100)),
                ('pricePerNight', models.IntegerField(default=150)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('USD', 'EUR')], default='USD', max_length=10)),
                ('maxOccupancy', models.IntegerField(default=1)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]