# Generated by Django 3.0.7 on 2020-06-19 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200616_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='code_link',
            new_name='links',
        ),
    ]
