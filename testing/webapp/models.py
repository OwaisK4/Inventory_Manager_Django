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

class Asset(models.Model):
    class STATUSES(models.TextChoices):
        checked_in = 'I', 'Checked in'
        checked_out = 'O', 'Checked out'

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField(help_text='Price of asset in rupees')
    purchase_date = models.DateField(help_text='Date of asset purchase')
    checkout_status = models.CharField(max_length=1, choices=STATUSES.choices, default=STATUSES.checked_in)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    asset_image = models.ImageField(upload_to='images/', null=True, blank=True)

    # class Meta:
    #     ordering = ['-purchase_date']

    def __str__(self):
        return f"{self.manufacturer.name} {self.name}"

    def get_absolute_url(self):
        return reverse('view_inventory-detail', args=[str(self.id)])