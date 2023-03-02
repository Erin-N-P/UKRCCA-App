# Generated by Django 4.1.5 on 2023-02-28 13:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_rule_truckclass_truck_ruleset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='gates_per_round',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='competition',
            name='no_of_rounds',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
    ]
