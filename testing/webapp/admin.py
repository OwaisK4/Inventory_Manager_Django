from django.contrib import admin
from .models import Asset, Category, Manufacturer, Department, Employee, Status
# Register your models here.

admin.site.register(Asset)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Department)
admin.site.register(Status)
admin.site.register(Employee)