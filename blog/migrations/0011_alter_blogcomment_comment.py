# Generated by Django 3.2.5 on 2021-08-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogcomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
