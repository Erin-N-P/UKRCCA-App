# Generated by Django 4.1.5 on 2023-03-05 20:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_rename_score_score_comp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='round',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Please enter a number greater than or equal to 1'), django.core.validators.MaxValueValidator(30, message='Please enter a number less than or equal to 30')]),
        ),
    ]