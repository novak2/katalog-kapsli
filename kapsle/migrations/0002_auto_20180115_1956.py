# Generated by Django 2.0 on 2018-01-15 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kapsle', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coin',
            options={'ordering': ['year', 'wiki_index']},
        ),
    ]
