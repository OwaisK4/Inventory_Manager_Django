# Generated by Django 4.2.3 on 2023-07-19 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_supplier_asset_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('M', 'Maintenance'), ('R', 'Repair'), ('U', 'Upgrade'), ('T', 'Test'), ('H', 'Hardware'), ('S', 'Software')], default='M', max_length=1)),
                ('maintenance_name', models.CharField(help_text='Maintenance name', max_length=200)),
                ('start_date', models.DateField(help_text='Starting date of maintenance')),
                ('end_date', models.DateField(help_text='Ending date of maintenance')),
                ('cost', models.IntegerField(help_text='Cost of maintenance in rupees')),
                ('notes', models.CharField(blank=True, help_text='Notes regarding maintenance', max_length=500)),
                ('file', models.FileField(upload_to='maintenance/')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.asset')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.supplier')),
            ],
        ),
    ]
