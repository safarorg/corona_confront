# Generated by Django 2.2.12 on 2020-04-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20200408_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='reimburse',
            name='thumb',
            field=models.ImageField(default='static/default_image.jpg', upload_to='images/'),
        ),
    ]
