import datetime
from django import forms
from webapp.models import Asset, Employee, Category, Manufacturer, Department, Status

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
        fields = ['category', 'manufacturer', 'name', 'price', 'purchase_date', 'status', 'checkout_status', 'department', 'assigned_to', 'asset_image']
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

            'purchase_date' : forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                # 'class': "form-control",
                'class': "datepicker form-control",
                'placeholder': 'Purchase Date (mm/dd/YYYY)',
                'type': 'date',
                # 'type': "datetime-local",
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
                # 'placeholder': 'Department',
            }),
            'asset_image' : forms.ClearableFileInput(attrs={
                # 'class': 'form-control',
                # 'required': "false"
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