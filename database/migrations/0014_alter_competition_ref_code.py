# Generated by Django 4.1.5 on 2023-03-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_alter_competition_ref_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='ref_code',
            field=models.CharField(blank=True, default='5XADK', editable=False, max_length=5, unique=True),
        ),
    ]
