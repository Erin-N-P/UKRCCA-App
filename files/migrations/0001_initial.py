# Generated by Django 2.2.12 on 2023-02-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=30)),
                ('sName', models.CharField(max_length=30)),
                ('tName', models.CharField(max_length=50)),
            ],
        ),
    ]
