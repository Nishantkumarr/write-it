# Generated by Django 3.0.7 on 2020-06-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200620_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='para_1',
        ),
        migrations.AddField(
            model_name='post',
            name='para_2',
            field=models.TextField(default='content'),
        ),
        migrations.AddField(
            model_name='post',
            name='para_3',
            field=models.TextField(default='content'),
        ),
    ]
