# Generated by Django 4.2.3 on 2023-07-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_alter_activity_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='asset_string',
            field=models.CharField(blank=True, help_text='Asset string', max_length=500),
        ),
    ]