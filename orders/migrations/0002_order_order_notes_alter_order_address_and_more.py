# Generated by Django 4.0.2 on 2023-02-12 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_notes',
            field=models.CharField(blank=True, max_length=700, verbose_name='Order Note'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=700, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Is Paid?'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
