# Generated by Django 4.1.5 on 2023-03-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_competition_ref_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='ref_code',
            field=models.CharField(blank=True, default='6UZNB', editable=False, max_length=10, unique=True),
        ),
    ]
