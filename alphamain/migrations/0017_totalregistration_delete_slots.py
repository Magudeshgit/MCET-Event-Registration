# Generated by Django 4.2.6 on 2023-11-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alphamain', '0016_alter_paperpresentation_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='slots',
        ),
    ]