# Generated by Django 2.0 on 2018-01-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapsle', '0006_auto_20180115_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='brewery_name',
            field=models.CharField(max_length=40),
        ),
    ]
