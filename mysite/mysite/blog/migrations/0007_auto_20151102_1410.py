# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_ctime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ctime',
            field=models.DateTimeField(null=True),
        ),
    ]
