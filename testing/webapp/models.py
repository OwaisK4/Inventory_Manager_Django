from django.db import models
from django.urls import reverse

# Create your models here.
class Asset(models.Model):
    class CATEGORIES(models.TextChoices):
        Laptop = 'L', 'Laptop'
        Workstation = 'W', 'Workstation'
    class COMPANIES(models.TextChoices):
        Dell = 'D', 'Dell'
        HP = 'H', 'HP'
        Lenovo = 'L', 'Lenovo'
    class STATUS(models.TextChoices):
        checked_in = 'I', 'Checked in'
        checked_out = 'O', 'Checked out'
    class DEPARTMENTS(models.TextChoices):
        Operations = 'O', 'Operations'
        Sales = 'S', 'Sales'
        Accounting = 'A', 'Accounting'
        IT = 'I', 'IT'

    category = models.CharField(max_length=1, choices=CATEGORIES.choices, default=CATEGORIES.Laptop, help_text='Type of asset (Laptop or Workstation)')
    manufacturer = models.CharField(max_length=1, choices=COMPANIES.choices, default=COMPANIES.HP, help_text='Manufacturer of asset (HP, DELL, Lenovo, etc)')
    name = models.CharField(max_length=200)
    price = models.IntegerField(help_text='Price of asset in rupees')
    purchase_date = models.DateField(help_text='Date of asset purchase')
    status = models.CharField(max_length=1, choices=STATUS.choices, default=STATUS.checked_in)
    department = models.CharField(max_length=1, choices=DEPARTMENTS.choices)

    class Meta:
        ordering = ['-purchase_date']

    def __str__(self):
        return f"{self.manufacturer} {self.name}"

    def get_absolute_url(self):
        return reverse('asset-detail', args=[str(self.id)])