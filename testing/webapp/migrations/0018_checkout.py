# Generated by Django 4.2.3 on 2023-07-25 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0017_location_accessory_location_asset_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('M', 'Maintenance'), ('I', 'Check-in'), ('O', 'Check-out')], max_length=1)),
                ('checkout_date', models.DateField(default=django.utils.timezone.now, help_text='Checkout/checkin date of asset')),
                ('expected_return_date', models.DateField(default=django.utils.timezone.now, help_text='Expected return date of asset')),
                ('condition', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], help_text='Condition of asset')),
                ('asset_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('notes', models.CharField(blank=True, help_text='Notes regarding checkout', max_length=500)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.asset')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.department')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.employee')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.location')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
