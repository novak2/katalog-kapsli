# Generated by Django 2.0 on 2018-01-15 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kapsle', '0004_auto_20180115_2039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercoin',
            options={'ordering': ['-coin__year']},
        ),
    ]