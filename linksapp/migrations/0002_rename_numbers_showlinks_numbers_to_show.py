# Generated by Django 4.0.1 on 2022-01-07 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linksapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showlinks',
            old_name='numbers',
            new_name='numbers_to_show',
        ),
    ]
