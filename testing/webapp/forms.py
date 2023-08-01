from django import forms
from webapp.models import Asset, Employee, Category, Manufacturer, Department, Status, Attachement, Supplier, Maintenance, Accessory, Location, Checkout, Audit, ScheduledAudit, License
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=100, help_text='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=100, help_text='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'User',
            }),
        }

class AssetModelForm(forms.ModelForm):
    def clean_price(self):
        price_input = self.cleaned_data['price']
        if price_input < 0:
            raise ValidationError(_("Price cannot be less than zero."))
        return price_input

    class Meta:
        model = Asset
        fields = ['category', 'manufacturer', 'name', 'price', 'processor', 'ram', 'hdd', 'ssd', 'purchase_date', 'status', 'department', 'supplier', 'assigned_to', 'location', 'asset_image', 'serial', 'invoice']
        widgets = {
            'category' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'manufacturer' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
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
            # 'checkout_status' : forms.Select(attrs={
            #     'class': "selectpicker",
            #     'data-style': "btn btn-info",
            #     'style': 'max-width: 300px;',
            #     'placeholder': 'Status',
            # }),
            'assigned_to' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'location' : forms.Select(attrs={
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

class AccessoryModelForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['category', 'manufacturer', 'name', 'price', 'purchase_date', 'status', 'department', 'supplier', 'assigned_to', 'location', 'accessory_image', 'serial', 'invoice']
        widgets = {
            'category' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'manufacturer' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name',
            }),
            'price' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Price',
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
            'assigned_to' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'location' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'department' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'accessory_image' : forms.ClearableFileInput(attrs={
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

class LicenseModelForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ["software_name", "to_name", "to_email", "license_type", "seats", "reference_no", "purchase_date", "expiration_date", "cost", "billing_terms", "notes"]
        widgets = {
            'software_name' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Software name',
            }),
            'to_name' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Licensed to',
            }),
            'to_email' : forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'user@email.com',
            }),
            'license_type' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'seats' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'No. of seats',
            }),
            'reference_no' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Reference number',
            }),
            'purchase_date' : forms.DateInput(
                attrs={
                'class': "datepicker form-control",
                'placeholder': 'Purchase Date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'expiration_date' : forms.DateInput(
                attrs={
                'class': "datepicker form-control",
                'placeholder': 'Expiration Date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'cost' : forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Cost in dollars',
            }),
            'billing_terms' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Billing terms',
            }),
            'notes' : forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Notes',
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

class CheckoutModelForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['employee', 'checkout_date', 'status', 'expected_return_date', 'condition', 'notes', 'asset_image', 'location', 'department']
        widgets = {
            'employee' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                'placeholder': 'Employee',
            }),
            'status' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                'placeholder': 'Status',
            }),
            'checkout_date' : forms.DateInput(
                attrs={
                'class': "datepicker form-control",
                'placeholder': 'Start date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'expected_return_date' : forms.DateInput(
                attrs={
                'class': "datepicker form-control",
                'placeholder': 'End date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'condition' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                'placeholder': 'Type',
            }),
            'notes' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Notes',
            }),
            'asset_image' : forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'location' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
            'department' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
            }),
        }

class AuditModelForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = ['purpose', 'audit_date', 'reason', 'results', 'file']
        widgets = {
            'purpose' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                'placeholder': 'Purpose',
            }),
            'audit_date' : forms.DateInput(
                attrs={
                'class': "datepicker form-control",
                'placeholder': 'Audit date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'reason' : forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Reason',
            }),
            'results' : forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Results',
            }),
            'file' : forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

class ScheduledAuditModelForm(forms.ModelForm):
    class Meta:
        model = ScheduledAudit
        fields = ['next_audit_date', 'assigned_to_user']
        widgets = {
            'next_audit_date' : forms.DateInput(attrs={
                'class': "datepicker form-control",
                'placeholder': 'Next scheduled audit date (mm/dd/YYYY)',
                'type': 'date',
            }),
            'assigned_to_user' : forms.Select(attrs={
                'class': "selectpicker",
                'data-style': "btn btn-info",
                'style': 'max-width: 300px;',
                'placeholder': 'Purpose',
            })
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

class LocationModelForm(forms.ModelForm):
    def clean_name(self):
        name_input = self.cleaned_data['name']
        if Location.objects.filter(name=name_input).exists():
            raise ValidationError(_("Location already exists."))
        return name_input

    class Meta:
        model = Location
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Location',
            }),
        }