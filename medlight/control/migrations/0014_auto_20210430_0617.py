# Generated by Django 3.2 on 2021-04-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0013_auto_20210430_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='records',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]