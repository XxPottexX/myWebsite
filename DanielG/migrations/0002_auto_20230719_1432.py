# Generated by Django 3.2.19 on 2023-07-19 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DanielG', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
