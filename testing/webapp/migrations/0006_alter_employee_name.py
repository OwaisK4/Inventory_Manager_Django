# Generated by Django 4.2.3 on 2023-07-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_asset_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(help_text='Name of employee', max_length=200, unique=True),
        ),
    ]
