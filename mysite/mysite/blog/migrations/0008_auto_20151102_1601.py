# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151102_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ctime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
