# Generated by Django 2.2.12 on 2020-04-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_reimburse_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reimburse',
            name='thumb',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
