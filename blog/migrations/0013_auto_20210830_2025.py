# Generated by Django 3.2.5 on 2021-08-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210820_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body_text',
            field=models.TextField(default=None, null=True),
        ),
    ]
