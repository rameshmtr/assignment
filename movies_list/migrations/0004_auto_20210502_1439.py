# Generated by Django 3.2 on 2021-05-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0003_alter_collections_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collections',
            name='movies',
        ),
        migrations.AddField(
            model_name='collections',
            name='movies',
            field=models.ManyToManyField(to='movies_list.Movies'),
        ),
    ]
