# Generated by Django 3.2 on 2021-05-02 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_auto_20210502_0938'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('username', 'password')},
        ),
    ]
