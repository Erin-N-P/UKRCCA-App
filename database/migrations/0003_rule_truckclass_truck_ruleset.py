# Generated by Django 4.1.5 on 2023-02-10 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_remove_truckclass_truck_delete_rule_delete_ruleset_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TruckClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('truck_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.truckclass')),
            ],
        ),
        migrations.CreateModel(
            name='Ruleset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.rule')),
            ],
        ),
    ]
