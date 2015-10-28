# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0002_blogspost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogsPost',
        ),
    ]
