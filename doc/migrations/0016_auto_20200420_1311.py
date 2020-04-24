# Generated by Django 3.0.5 on 2020-04-20 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0015_auto_20200418_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date', 'title'), 'verbose_name': 'Новина', 'verbose_name_plural': 'Новини'},
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Посилання'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 20), verbose_name='Дата'),
        ),
    ]
