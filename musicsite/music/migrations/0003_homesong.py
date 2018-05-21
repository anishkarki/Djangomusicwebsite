# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=250)),
                ('audio_file', models.FileField(default='', upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
