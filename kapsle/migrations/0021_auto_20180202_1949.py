# Generated by Django 2.0 on 2018-02-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapsle', '0020_auto_20180202_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoincondition',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usercoinkind',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usercointype',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]