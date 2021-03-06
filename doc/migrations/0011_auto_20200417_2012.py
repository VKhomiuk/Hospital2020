# Generated by Django 3.0.5 on 2020-04-17 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0010_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 17), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='news/logo.png', upload_to='news/', verbose_name='Зображення'),
        ),
    ]
