# Generated by Django 2.2 on 2020-12-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20201203_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='answer',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='content',
            name='question',
            field=models.TextField(default=''),
        ),
    ]
