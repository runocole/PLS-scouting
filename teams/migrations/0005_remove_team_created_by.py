# Generated by Django 5.1.7 on 2025-06-23 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0004_team_created_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="created_by",
        ),
    ]
