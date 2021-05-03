# Generated by Django 3.2 on 2021-05-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, unique=True)),
                ('description', models.CharField(max_length=240, unique=True)),
                ('genres', models.CharField(max_length=24, unique=True)),
            ],
        ),
    ]