# Generated by Django 4.1.5 on 2023-03-10 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_remove_ruleset_rule_rule_ruleset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='ruleset',
        ),
    ]
