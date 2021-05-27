# Generated by Django 3.2 on 2021-05-27 04:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control', '0021_auto_20210514_1730'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='patients',
            unique_together={('author', 'full_name', 'date', 'phone')},
        ),
    ]
