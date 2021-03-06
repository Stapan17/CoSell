# Generated by Django 3.2.7 on 2021-09-26 16:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CosellApp', '0003_auto_20210926_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('Photo', models.ImageField(default='NotsetDefaultPicture.jpg', upload_to='profile_pics')),
                ('SellerInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CosellApp.student')),
            ],
        ),
    ]
