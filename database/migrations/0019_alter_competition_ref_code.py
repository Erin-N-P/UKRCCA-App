# Generated by Django 4.1.5 on 2023-03-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_alter_competition_ref_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='ref_code',
            field=models.CharField(blank=True, default='BLU6O', editable=False, max_length=10, unique=True),
        ),
    ]
