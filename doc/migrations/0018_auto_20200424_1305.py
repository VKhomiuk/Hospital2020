# Generated by Django 3.0.5 on 2020-04-24 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0017_auto_20200423_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 24), verbose_name='Дата'),
        ),
    ]