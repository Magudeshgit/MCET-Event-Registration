# Generated by Django 4.2.6 on 2023-11-02 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuitry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Civiathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
                ('member3', models.CharField(max_length=50)),
                ('roll3', models.CharField(blank=True, max_length=20)),
                ('member4', models.CharField(max_length=50)),
                ('roll4', models.CharField(blank=True, max_length=20)),
                ('member5', models.CharField(max_length=50)),
                ('roll5', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CodeClueCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
                ('member3', models.CharField(max_length=50)),
                ('roll3', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('datetime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ideathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicname', models.CharField(max_length=100)),
                ('teamsize', models.CharField(max_length=50)),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
                ('member3', models.CharField(max_length=50)),
                ('roll3', models.CharField(blank=True, max_length=20)),
                ('member4', models.CharField(max_length=50)),
                ('roll4', models.CharField(blank=True, max_length=20)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mechmania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
                ('member3', models.CharField(max_length=50)),
                ('roll3', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='odetocode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PaperPresentationIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('papername', models.CharField(max_length=100)),
                ('teamsize', models.CharField(max_length=50)),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductPitching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=100)),
                ('teamsize', models.CharField(max_length=50)),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='studentlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('event1', models.CharField(max_length=50)),
                ('event2', models.CharField(max_length=50)),
                ('event3', models.CharField(max_length=50)),
                ('event4', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SyntaxSmackdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Techtales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPresentationIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=100)),
                ('teamsize', models.CharField(max_length=50)),
                ('member1', models.CharField(max_length=50)),
                ('roll1', models.CharField(blank=True, max_length=20)),
                ('member2', models.CharField(max_length=50)),
                ('roll2', models.CharField(blank=True, max_length=20)),
                ('about', models.TextField()),
                ('timeslot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alphamain.slots')),
            ],
        ),
    ]
