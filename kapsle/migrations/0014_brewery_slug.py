# Generated by Django 2.0 on 2018-01-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapsle', '0013_auto_20180129_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='slug',
            field=models.SlugField(default='null'),
            preserve_default=False,
        ),
    ]
