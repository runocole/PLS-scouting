# Generated by Django 5.1.7 on 2025-07-07 22:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
        ('teams', '0005_remove_team_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together={('team', 'author')},
        ),
    ]
