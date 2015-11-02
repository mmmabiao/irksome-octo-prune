# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151101_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
