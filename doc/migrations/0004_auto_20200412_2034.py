# Generated by Django 3.0.5 on 2020-04-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0003_reception'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='date',
            field=models.DateTimeField(auto_created=True, verbose_name='Дата'),
        ),
    ]
