# Generated by Django 2.0 on 2018-01-29 05:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapsle', '0011_remove_usercoin_to_own'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='ignored_by',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
