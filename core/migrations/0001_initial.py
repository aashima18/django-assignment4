# Generated by Django 2.2.6 on 2019-10-08 06:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=254, unique=True)),
                ('contact_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('street_name', models.CharField(max_length=254)),
                ('suburb', models.CharField(max_length=254)),
                ('postcode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,10}$')])),
            ],
        ),
    ]
