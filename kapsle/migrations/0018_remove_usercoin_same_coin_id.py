# Generated by Django 2.0 on 2018-01-31 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kapsle', '0017_usercoin_same_coin_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoin',
            name='same_coin_id',
        ),
    ]
