# Generated by Django 4.2.3 on 2023-07-26 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0029_alter_activity_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-id']},
        ),
    ]
