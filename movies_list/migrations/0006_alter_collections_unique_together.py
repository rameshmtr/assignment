# Generated by Django 3.2 on 2021-05-02 15:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies_list', '0005_auto_20210502_1444'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='collections',
            unique_together={('user',)},
        ),
    ]
