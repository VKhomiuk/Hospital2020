# Generated by Django 3.0.5 on 2020-04-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0005_auto_20200412_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('annotation', models.CharField(max_length=255, verbose_name='Короткий опис')),
                ('text', models.TextField(verbose_name='Основна частина')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
                'ordering': ('title', 'date'),
            },
        ),
    ]