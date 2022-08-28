# Generated by Django 4.1 on 2022-08-27 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MonsterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('monster_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapsapi.monsteruser')),
            ],
        ),
        migrations.CreateModel(
            name='MonsterSpotting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster_date', models.DateTimeField(max_length=50)),
                ('monster_time', models.TimeField(max_length=25)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapsapi.location')),
                ('monster_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapsapi.monsteruser')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapsapi.species')),
            ],
        ),
    ]
