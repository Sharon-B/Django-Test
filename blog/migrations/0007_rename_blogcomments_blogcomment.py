# Generated by Django 3.2.5 on 2021-08-19 14:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20210819_1416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogComments',
            new_name='BlogComment',
        ),
    ]
