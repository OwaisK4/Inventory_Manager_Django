from django.db import models
from django.urls import reverse

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