# Generated by Django 3.1.4 on 2021-10-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CosellApp', '0006_auto_20211002_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='college_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.CharField(choices=[('IIITV', 'Indian Institute of Information Technology Vadodara (Gandhinagar Campus)'), ('IITB', 'Indian Institute of Technology Bombay'), ('IIITL', 'Indian Institute of Information Technology Lucknow'), ('IITK', 'Indian Institute of Technology Kanpur'), ('GEC', 'Government Engineering College,Gandhinagar')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]
