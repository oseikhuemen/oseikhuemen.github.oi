# Generated by Django 2.2 on 2020-12-03 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mask',
            new_name='Question',
        ),
    ]