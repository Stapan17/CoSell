# Generated by Django 3.1.4 on 2021-10-23 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosellApp', '0014_auto_20211023_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='transection_id',
            field=models.CharField(max_length=30),
        ),
    ]