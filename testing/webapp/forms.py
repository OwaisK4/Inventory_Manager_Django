import datetime
from django import forms
from webapp.models import Asset, Employee, Category, Manufacturer, Department, Status, Attachement, Supplier, Maintenance

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        # Remember to always return the cleaned data.
        return data

class AssetModelForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['category', 'manufacturer', 'name', 'price', 'processor', 'ram', 'hdd', 'ssd', 'purchase_date', 'status', 'checkout_status', 'department', 'supplier', 'assigned_to', 'asset_image', 'serial', 'invoice']
        widgets = {
            'category' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                # 'label': 'Category',
                # 'placeholder': 'Category',
            }),
            'manufacturer' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                # 'placeholder': 'Manufacturer',
            }),
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name',
            }),
            'price' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Price',
            }),
            'processor' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Processor',
            }),
            'ram' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'RAM',
            }),
            'hdd' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'HDD',
            }),
            'ssd' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'SSD',
            }),
            'purchase_date' : forms.DateInput(
                # format=('%m/%d/%Y'),
                attrs={
                'class': "datepicker form-control",
                'placeholder': 'Purchase Date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'status' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'checkout_status' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                'placeholder': 'Status',
            }),
            'assigned_to' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'department' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'asset_image' : forms.ClearableFileInput(attrs={
                # 'class': 'form-control',
            }),
            'supplier' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'serial' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Serial no.',
            }),
            'invoice' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Invoice no.',
            }),
        }

class AttachementModelForm(forms.ModelForm):
    class Meta:
        model = Attachement
        fields = ['file']
        widgets = {
            'file':  forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }

class MaintenanceModelForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['type', 'supplier', 'maintenance_name', 'start_date', 'end_date', 'cost', 'notes', 'file']
        widgets = {
            'type' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                'placeholder': 'Type',
            }),
            'supplier' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'maintenance_name' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Maintenance name',
            }),
            'start_date' : forms.DateInput(
                attrs={
                'class': "datepicker form-control",
                'placeholder': 'Start date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'end_date' : forms.DateInput(
                attrs={
                'class': "datepicker form-control",
                'placeholder': 'End date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'cost' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Cost',
            }),
            'notes' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Notes',
            }),
            'file':  forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }


class EmployeeModelForm(forms.ModelForm):
    def clean_name(self):
        name_input = self.cleaned_data['name']
        if Employee.objects.filter(name=name_input).exists():
            raise ValidationError(_("Employee already exists."))
        return name_input

    class Meta:
        model = Employee
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name',
            }),
        }

class CategoryModelForm(forms.ModelForm):
    def clean_name(self):
        name_input = self.cleaned_data['name']
        if Category.objects.filter(name=name_input).exists():
            raise ValidationError(_("Category already exists."))
        return name_input

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Category',
            }),
        }

class ManufacturerModelForm(forms.ModelForm):
    def clean_name(self):
        name_input = self.cleaned_data['name']
        if Manufacturer.objects.filter(name=name_input).exists():
            raise ValidationError(_("Manufacturer already exists."))
        return name_input

    class Meta:
        model = Manufacturer
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Manufacturer',
            }),
        }

class SupplierModelForm(forms.ModelForm):
    def clean_name(self):
        name_input = self.cleaned_data['name']
        if Supplier.objects.filter(name=name_input).exists():
            raise ValidationError(_("Supplier already exists."))
        return name_input

    class Meta:
        model = Supplier
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Supplier',
            }),
        }

class DepartmentModelForm(forms.ModelForm):
    def clean_name(self):
        name_input = self.cleaned_data['name']
        if Supplier.objects.filter(name=name_input).exists():
            raise ValidationError(_("Department already exists."))
        return name_input

    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Department',
            }),
        }

class StatusModelForm(forms.ModelForm):
    def clean_name(self):
        name_input = self.cleaned_data['name']
        if Supplier.objects.filter(name=name_input).exists():
            raise ValidationError(_("Status already exists."))
        return name_input

    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Status',
            }),
        }