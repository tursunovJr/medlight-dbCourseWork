# Generated by Django 3.1.7 on 2021-03-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name='Имя Пользователя'),
        ),
    ]
