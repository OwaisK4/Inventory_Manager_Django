# Generated by Django 4.2.3 on 2023-07-31 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0032_alter_scheduledaudit_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledaudit',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_audit', to='webapp.asset'),
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='Time of change log')),
                ('status', models.CharField(help_text='Status', max_length=200)),
                ('user', models.CharField(help_text='User', max_length=200)),
                ('processor', models.CharField(help_text='Processor', max_length=200)),
                ('RAM', models.CharField(help_text='RAM', max_length=200)),
                ('disk_space', models.CharField(help_text='Disk space', max_length=200)),
                ('change_in_processor', models.CharField(help_text='Change in Processor', max_length=100)),
                ('change_in_ram', models.CharField(help_text='Change in RAM', max_length=100)),
                ('change_in_disk', models.CharField(help_text='Change in Disk', max_length=100)),
                ('message', models.CharField(help_text='Message', max_length=500)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.asset')),
            ],
        ),
    ]