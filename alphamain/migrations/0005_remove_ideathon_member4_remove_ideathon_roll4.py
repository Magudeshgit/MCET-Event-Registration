# Generated by Django 4.2.6 on 2023-11-02 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alphamain', '0004_ideathon_teamname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideathon',
            name='member4',
        ),
        migrations.RemoveField(
            model_name='ideathon',
            name='roll4',
        ),
    ]
