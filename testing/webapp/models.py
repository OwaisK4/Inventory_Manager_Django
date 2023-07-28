from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Type of asset", unique=True)
    def __str__(self):
        return f"{self.name}"
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=200, help_text="Name of manufacturing company", unique=True)
    def __str__(self):
        return f"{self.name}"
    
class Status(models.Model):
    name = models.CharField(max_length=200, help_text="Status of asset", unique=True)
    def __str__(self):
        return f"{self.name}"

class Department(models.Model):
    name = models.CharField(max_length=200, help_text="Name of department", unique=True)
    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=200, help_text="Name of employee", unique=True)
    def __str__(self):
        return f"{self.name}"

class Supplier(models.Model):
    name = models.CharField(max_length=200, help_text="Supplier of asset/accessory", unique=True)
    def __str__(self):
        return f"{self.name}"
class Location(models.Model):
    name = models.CharField(max_length=200, help_text="Location name", unique=True)
    def __str__(self):
        return f"{self.name}"

class Asset(models.Model):
    class STATUSES(models.TextChoices):
        checked_in = 'I', 'Checked in'
        checked_out = 'O', 'Checked out'

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, help_text='Name of asset')
    price = models.IntegerField(help_text='Price of asset in rupees')

    processor = models.CharField(max_length=200, help_text='Processor specs')
    ram = models.IntegerField(help_text='Total RAM in asset')
    hdd = models.IntegerField(help_text='Total HDD storage in asset', blank=True, null=True)
    ssd = models.IntegerField(help_text='Total SSD storage in asset', blank=True, null=True)

    purchase_date = models.DateField(help_text='Date of asset purchase')
    checkout_status = models.CharField(max_length=1, choices=STATUSES.choices, default=STATUSES.checked_in)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    asset_image = models.ImageField(upload_to='images/', blank=True, null=True)

    serial = models.CharField(max_length=200, help_text='Serial number of asset', blank=True)
    invoice = models.IntegerField(help_text='Invoice number of asset', blank=True, null=True)

    # class Meta:
    #     ordering = ['-purchase_date']

    def __str__(self):
        return f"{self.manufacturer.name} {self.name}"

    def get_absolute_url(self):
        return reverse('view_inventory-detail', args=[str(self.id)])
    
class Attachement(models.Model):
    file = models.FileField(upload_to='attachements/')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

class Maintenance(models.Model):
    class TYPES(models.TextChoices):
        maintenance = 'M', 'Maintenance'
        repair = 'R', 'Repair'
        upgrade = 'U', 'Upgrade'
        test = 'T', 'Test'
        hardware = 'H', 'Hardware'
        software = 'S', 'Software'

    type = models.CharField(max_length=1, choices=TYPES.choices, default=TYPES.maintenance)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    maintenance_name = models.CharField(max_length=200, help_text="Maintenance name")
    start_date = models.DateField(help_text='Starting date of maintenance')
    end_date = models.DateField(help_text='Ending date of maintenance')
    cost = models.IntegerField(help_text='Cost of maintenance in rupees')
    notes = models.CharField(max_length=500, help_text="Notes regarding maintenance", blank=True)
    file = models.FileField(upload_to='maintenance/')

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

class Checkout(models.Model):
    class TYPES(models.TextChoices):
        IN = 'I', 'Check-in'
        OUT = 'O', 'Check-out'
        
    type = models.CharField(max_length=1, choices=TYPES.choices)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    checkout_date = models.DateField(help_text='Checkout/checkin date of asset', default=timezone.now)
    expected_return_date = models.DateField(help_text='Expected return date of asset', default=timezone.now, blank=True, null=True)
    condition = models.IntegerField(choices=[(i, i) for i in range(1, 11)], help_text="Condition of asset")
    asset_image = models.ImageField(upload_to='images/', blank=True, null=True)
    notes = models.CharField(max_length=500, help_text="Notes regarding checkout", blank=True)

    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-id']

class Activity(models.Model):
    class TYPES(models.TextChoices):
        asset = 's', 'Asset'
        accessory = 'c', 'Accessory'
    timestamp = models.DateTimeField(help_text='Checkout/checkin date of asset', auto_now_add=True)
    type = models.CharField(max_length=1, choices=TYPES.choices, default=TYPES.asset)
    event = models.CharField(max_length=50, help_text="Event")
    notes = models.CharField(max_length=500, help_text="Notes regarding activity", blank=True)
    asset_string = models.CharField(max_length=500, help_text="Asset string", blank=True)

    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    asset = models.ForeignKey(Asset, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-id']

class Audit(models.Model):
    class TYPES(models.TextChoices):
        general = 'G', 'General'
        Special = 'S', 'Special'
    purpose = models.CharField(max_length=1, choices=TYPES.choices, default=TYPES.general)
    audit_date = models.DateField(help_text='Audit date of asset', default=timezone.now)
    reason = models.CharField(max_length=200, help_text="Reason for (special) audit", blank=True) # Only for special audits
    results = models.CharField(max_length=500, help_text="Results of audit") # Use TextArea widget for this
    file = models.FileField(upload_to='audits/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    asset_string = models.CharField(max_length=500, help_text="Asset string", blank=True)

    class Meta:
        ordering = ['-id']

class ScheduledAudit(models.Model):
    def date_in_future():
        now = timezone.now()
        return now + datetime.timedelta(weeks=4)
    
    next_audit_date = models.DateField(help_text='Audit date of asset', default=date_in_future)
    assigned_to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='scheduled_audit')

    class Meta:
        ordering = ['-next_audit_date', '-id']

class Change(models.Model):
    timestamp = models.DateTimeField(help_text='Time of change log', auto_now_add=True)
    status = models.CharField(max_length=200, help_text="Status")
    user = models.CharField(max_length=200, help_text="User")
    processor = models.CharField(max_length=200, help_text="Processor")
    RAM = models.CharField(max_length=200, help_text="RAM")
    disk_space = models.CharField(max_length=200, help_text="Disk space")
    change_in_processor = models.CharField(max_length=100, help_text="Change in Processor")
    change_in_ram = models.CharField(max_length=100, help_text="Change in RAM")
    change_in_disk = models.CharField(max_length=100, help_text="Change in Disk")
    message = models.CharField(max_length=500, help_text="Message")

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

class Accessory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, help_text='Name of asset')
    price = models.IntegerField(help_text='Price of asset in rupees')

    purchase_date = models.DateField(help_text='Date of asset purchase')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    accessory_image = models.ImageField(upload_to='images/', blank=True, null=True)

    serial = models.CharField(max_length=200, help_text='Serial number of asset', blank=True)
    invoice = models.IntegerField(help_text='Invoice number of asset', blank=True, null=True)

    def __str__(self):
        return f"{self.manufacturer.name} {self.name}"