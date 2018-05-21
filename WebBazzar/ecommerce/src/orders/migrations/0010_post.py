# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hitcount.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20150903_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
    ]
