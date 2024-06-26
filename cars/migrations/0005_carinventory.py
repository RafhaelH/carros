# Generated by Django 5.0.3 on 2024-04-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_rename_phto_car_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('cars_count', models.IntegerField()),
                ('cars_values', models.FloatField()),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
