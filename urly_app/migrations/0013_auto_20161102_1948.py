# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urly_app', '0012_auto_20161102_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_base',
            field=models.URLField(default=b'http://www.spe.org/go/', max_length=18, choices=[(b'http://www.spe.org/go/', b'SPE.org/go'), (b'http://go.spe.org/', b'GO.spe.org'), (b'http://2s.pe/', b'2s.pe'), (b'http://4s.pe/', b'4s.pe')]),
        ),
    ]
