# Generated by Django 4.0.2 on 2023-02-19 10:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_datetime_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 19, 10, 30, 42, 595687, tzinfo=utc)),
        ),
    ]
