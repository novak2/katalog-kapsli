# Generated by Django 2.0 on 2018-01-28 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kapsle', '0010_auto_20180128_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoin',
            name='to_own',
        ),
    ]
