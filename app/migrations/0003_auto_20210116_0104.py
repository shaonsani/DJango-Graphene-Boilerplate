# Generated by Django 3.1.5 on 2021-01-15 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210116_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='catagory',
            new_name='category',
        ),
    ]
