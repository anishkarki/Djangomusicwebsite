# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_productfeatured_text_css_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
