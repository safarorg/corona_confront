# Generated by Django 2.2.12 on 2020-04-11 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_auto_20200411_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reimburse',
            name='address_two',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
