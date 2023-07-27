from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from datetime import datetime
from django.utils import timezone
from .models import Asset, Employee, Category, Manufacturer, Department, Status, Attachement, Supplier, Maintenance, Accessory, Location, Checkout, Activity, Audit, ScheduledAudit
from .forms import AssetModelForm, EmployeeModelForm, CategoryModelForm, ManufacturerModelForm, AttachementModelForm, SupplierModelForm, DepartmentModelForm, StatusModelForm, MaintenanceModelForm, AccessoryModelForm, LocationModelForm, RegistrationForm, CheckoutModelForm, AuditModelForm, ScheduledAuditModelForm
# from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import qrcode
from io import BytesIO
from base64 import b64encode
import openpyxl

# Create your views here.
def index(request):
    return HttpResponse("<H2>HEY! Welcome to my website! </H2>")

@login_required
def master_page(request):
    return render(request, 'master.html')

@login_required
def about(request):
    return render(request, 'registration/about.html')

@login_required
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class UserListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'registration/view_users.html'

@login_required
def input_inventory_form(request):
    if request.method == 'POST':
        form = AssetModelForm(request.POST, request.FILES)
        if form.is_valid():
            created_asset = form.save(commit=False)
            activity = Activity(event="Create", user=request.user)
            activity.asset = created_asset
            activity.asset_string = str(created_asset)
            activity.employee = created_asset.assigned_to
            created_asset.save()
            activity.save()
            redirect_to = request.POST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('view_inventory-list'))
    else:
        form = AssetModelForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'webapp/input_inventory.html', context)

@login_required
def input_employee_form(request):
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            redirect_to = request.POST.get('next', '')
            if redirect_to:
                return HttpResponseRedirect(redirect_to)
            else:
                return HttpResponseRedirect(reverse('view_employee-list'))
    else:
        form = EmployeeModelForm(request.POST)
    context = {
        'form': form,
        'next': request.GET.get('next', '')
    }
    return render(request, 'webapp/input_employee.html', context)

class InventoryListView(LoginRequiredMixin, ListView):
    model = Asset
    context_object_name = 'inventory'
    template_name = 'webapp/view_inventory.html'

class InventoryDetailView(LoginRequiredMixin, DetailView):
    model = Asset
    context_object_name = 'asset'
    template_name = 'webapp/view_inventory_detail.html'

class InventoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Asset
    fields = '__all__'
    context_object_name = 'asset'
    template_name = 'webapp/view_inventory_confirm_delete.html'
    success_url = reverse_lazy('view_inventory-list')

    def form_valid(self, form) -> HttpResponse:
        created_asset = self.get_object()
        activity = Activity(event="Delete", user=self.request.user)
        activity.asset = created_asset
        activity.asset_string = str(created_asset)
        activity.employee = created_asset.assigned_to
        activity.save()
        return super().form_valid(form)

class InventoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Asset
    context_object_name = 'asset'
    form_class = AssetModelForm
    template_name = 'webapp/input_inventory.html'
    success_url = reverse_lazy('view_inventory-list')
    
    def form_valid(self, form) -> HttpResponse:
        created_asset = form.save(commit=False)
        activity = Activity(event="Update", user=self.request.user)
        activity.asset = created_asset
        activity.asset_string = str(created_asset)
        activity.employee = created_asset.assigned_to
        activity.save()
        return super().form_valid(form)

@login_required
def generate_barcode(request, pk):
    asset = Asset.objects.get(pk=pk)
    barcode = qrcode.make("LDP " + str(asset.id) + " " + asset.name)
    response = HttpResponse(content_type='image/jpg')
    barcode.save(response, "JPEG")
    # response['Content-Disposition'] = 'attachment; filename="piece.jpg"'
    return response

@login_required
def generate_all_barcodes(request):
    assets = Asset.objects.all()
    images = []
    for asset in assets:
        barcode = qrcode.make("LDP " + str(asset.id) + " " + asset.name)
        image = BytesIO()
        barcode.save(image, format="JPEG")
        dataurl = 'data:image/png;base64,' + b64encode(image.getvalue()).decode('ascii')
        images.append(dataurl)


    context = {
        'images': images
    }
    return render(request, 'webapp/view_barcodes.html', context)

# @login_required
# def inventory_checkout(request, pk):
#     asset = Asset.objects.get(pk=pk)
#     if asset.checkout_status == 'I':
#         Asset.objects.filter(pk=pk).update(checkout_status='O')
#     else:
#         Asset.objects.filter(pk=pk).update(checkout_status='I')
#     return HttpResponseRedirect(reverse('view_inventory-list'))

@login_required
def inventory_attachements_list(request, pk):
    asset = Asset.objects.get(pk=pk)
    attachements = Attachement.objects.filter(asset=asset)
    context = {
        'asset': asset,
        'attachements': attachements,
    }
    return render(request, 'webapp/view_inventory_attachements.html', context)

@login_required
def inventory_attachements_delete(request, pk, pk_attachement):
    # Attachement.objects.filter(pk=pk_attachement).delete()
    attachement = Attachement.objects.get(pk=pk_attachement)
    attachement.delete()
    return HttpResponseRedirect(reverse('view_inventory-attachements-list', args=(str(pk),)))

class InventoryAttachementsAddView(LoginRequiredMixin, CreateView):
    model = Attachement
    form_class = AttachementModelForm
    template_name = 'webapp/view_inventory_input_attachements.html'

    def get_success_url(self) -> str:
        if self.kwargs['pk']:
            return reverse('view_inventory-attachements-list', args=str(self.kwargs['pk'],))
        else:
            return super().get_success_url()

    def form_valid(self, form):
        attachement = form.save(commit=False)
        attachement.asset = Asset.objects.get(pk=self.kwargs['pk'])
        attachement.save()
        return HttpResponseRedirect(self.get_success_url())

@login_required
def inventory_maintenances_list(request, pk):
    asset = Asset.objects.get(pk=pk)
    maintenances = Maintenance.objects.filter(asset=asset)
    context = {
        'asset': asset,
        'maintenances': maintenances,
    }
    return render(request, 'webapp/view_inventory_maintenances.html', context)

@login_required
def inventory_maintenances_delete(request, pk, pk_maintenance):
    Maintenance.objects.filter(pk=pk_maintenance).delete()
    return HttpResponseRedirect(reverse('view_inventory-maintenances-list', args=(str(pk),)))

class InventoryMaintenancesAddView(LoginRequiredMixin, CreateView):
    model = Maintenance
    form_class = MaintenanceModelForm
    template_name = 'webapp/view_inventory_input_maintenances.html'

    def get_success_url(self) -> str:
        if self.kwargs['pk']:
            return reverse('view_inventory-maintenances-list', args=(self.kwargs['pk'],))
        else:
            return super().get_success_url()

    def form_valid(self, form):
        maintenance = form.save(commit=False)
        maintenance.asset = Asset.objects.get(pk=self.kwargs['pk'])
        maintenance.save()
        return HttpResponseRedirect(self.get_success_url())

@login_required
def inventory_checkout_list(request, pk):
    asset = Asset.objects.get(pk=pk)
    checkouts = Checkout.objects.filter(asset=asset)
    context = {
        'asset': asset,
        'checkouts': checkouts,
    }
    return render(request, 'webapp/view_inventory_checkout_log.html', context)

class CheckoutView(LoginRequiredMixin, CreateView):
    model = Checkout
    form_class = CheckoutModelForm
    template_name = 'webapp/view_inventory_checkout.html'

    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_inventory-checkout-list', args=str(self.kwargs['pk'],))

    def form_valid(self, form):
        checkout = form.save(commit=False)
        checkout.asset = Asset.objects.get(pk=self.kwargs['pk'])
        checkout.type = 'O'
        checkout.user = self.request.user
        checkout.save()
        Asset.objects.filter(pk=self.kwargs['pk']).update(checkout_status='O')
        return HttpResponseRedirect(self.get_success_url())

class CheckinView(LoginRequiredMixin, CreateView):
    model = Checkout
    form_class = CheckoutModelForm
    template_name = 'webapp/view_inventory_checkin.html'
    
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_inventory-checkout-list', args=str(self.kwargs['pk'],))
        
    def form_valid(self, form):
        checkin = form.save(commit=False)
        checkin.asset = Asset.objects.get(pk=self.kwargs['pk'])
        checkin.type = 'I'
        checkin.user = self.request.user
        checkin.save()
        Asset.objects.filter(pk=self.kwargs['pk']).update(checkout_status='I')
        return HttpResponseRedirect(self.get_success_url())
    
@login_required
def inventory_audit_list(request, pk):
    asset = Asset.objects.get(pk=pk)
    audits = Audit.objects.filter(asset=asset)
    context = {
        'asset': asset,
        'audits': audits,
    }
    return render(request, 'webapp/view_inventory_audit_log.html', context)

class InventoryAuditView(LoginRequiredMixin, CreateView):
    model = Audit
    form_class = AuditModelForm
    template_name = 'webapp/view_inventory_audit.html'

    def get_success_url(self) -> str:
        if self.kwargs['pk']:
            return reverse('view_inventory-audit-schedule', args=(self.kwargs['pk'],))
        else:
            return super().get_success_url()

    def form_valid(self, form):
        audit = form.save(commit=False)
        asset = Asset.objects.get(pk=self.kwargs['pk'])
        audit.asset = asset
        audit.asset_string = str(asset)
        audit.user = self.request.user
        audit.save()
        return HttpResponseRedirect(self.get_success_url())
    
class InventoryAuditScheduleView(LoginRequiredMixin, CreateView):
    model = ScheduledAudit
    form_class = ScheduledAuditModelForm
    template_name = 'webapp/view_inventory_audit_schedule.html'

    def get_success_url(self) -> str:
        if self.kwargs['pk']:
            return reverse('view_inventory-audit-list', args=(self.kwargs['pk'],))
        else:
            return super().get_success_url()

    def form_valid(self, form):
        scheduled_audit = form.save(commit=False)
        asset = Asset.objects.get(pk=self.kwargs['pk'])
        if asset.scheduled_audit.exists():
            asset.scheduled_audit.all().delete()
        scheduled_audit.asset = asset
        scheduled_audit.save()
        return HttpResponseRedirect(self.get_success_url())

class ScheduledAuditsListView(LoginRequiredMixin, ListView):
    model = ScheduledAudit
    context_object_name = 'scheduled_audits'
    template_name = 'webapp/view_inventory_scheduled_audits.html'

@login_required
def scheduled_audit_view(request, pk):
    audit = ScheduledAudit.objects.get(pk=pk)
    pk_asset = audit.asset.id
    # audit.delete()
    return HttpResponseRedirect(reverse('view_inventory-audit', args=(pk_asset,)))
    # context = {
    #     'asset': asset,
    #     'scheduled_audits': scheduled_audits,
    # }
    # return render(request, 'webapp/view_inventory_scheduled_audits.html', context)

class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity
    context_object_name = 'activities'
    template_name = 'webapp/view_activity_log.html'

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'webapp/view_employees.html'

# class EmployeeDetailView(DetailView):
#     model = Employee
#     context_object_name = 'employee'
#     template_name = 'webapp/view_employee_detail.html'

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    fields = '__all__'
    context_object_name = 'employee'
    template_name = 'webapp/view_employee_confirm_delete.html'
    success_url = reverse_lazy('view_employee-list')

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    context_object_name = 'employee'
    form_class = EmployeeModelForm
    template_name = 'webapp/input_employee.html'
    success_url = reverse_lazy('view_employee-list')

@login_required
def time_view(request):
    now = datetime.now()
    time = f"Current time is {now}"
    return HttpResponse(time)

# Views for Category objects
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    fields = '__all__'
    context_object_name = 'categories'
    template_name = 'webapp/view_categories.html'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'webapp/input_category.html'
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_category-list')

@login_required
def category_delete(request, pk):
    Category.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_category-list'))

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'webapp/input_category.html'
    success_url = reverse_lazy('view_category-list')

# Views for Manufacturer objects
class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    fields = '__all__'
    context_object_name = 'manufacturers'
    template_name = 'webapp/view_manufacturers.html'

class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    form_class = ManufacturerModelForm
    template_name = 'webapp/input_manufacturer.html'
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_manufacturer-list')

@login_required
def manufacturer_delete(request, pk):
    Manufacturer.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_manufacturer-list'))

class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    form_class = ManufacturerModelForm
    template_name = 'webapp/input_manufacturer.html'
    success_url = reverse_lazy('view_manufacturer-list')

# Views for Supplier objects
class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    fields = '__all__'
    context_object_name = 'suppliers'
    template_name = 'webapp/view_suppliers.html'

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierModelForm
    template_name = 'webapp/input_supplier.html'
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_supplier-list')

@login_required
def supplier_delete(request, pk):
    Supplier.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_supplier-list'))

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierModelForm
    template_name = 'webapp/input_supplier.html'
    success_url = reverse_lazy('view_supplier-list')

# Views for Department objects
class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    fields = '__all__'
    context_object_name = 'departments'
    template_name = 'webapp/view_departments.html'

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentModelForm
    template_name = 'webapp/input_department.html'
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_department-list')

@login_required
def department_delete(request, pk):
    Department.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_department-list'))

class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentModelForm
    template_name = 'webapp/input_department.html'
    success_url = reverse_lazy('view_department-list')

# Views for Status objects
class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    fields = '__all__'
    context_object_name = 'statuses'
    template_name = 'webapp/view_statuses.html'

class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusModelForm
    template_name = 'webapp/input_status.html'
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_status-list')

@login_required
def status_delete(request, pk):
    Status.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_status-list'))

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusModelForm
    template_name = 'webapp/input_status.html'
    success_url = reverse_lazy('view_status-list')

# Views for Accessory objects
class AccessoryCreateView(LoginRequiredMixin, CreateView):
    model = Accessory
    form_class = AccessoryModelForm
    template_name = 'webapp/input_accessory.html'
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_accessory-list')

class AccessoryListView(LoginRequiredMixin, ListView):
    model = Accessory
    context_object_name = 'accessories'
    template_name = 'webapp/view_accessory.html'

class AccessoryDetailView(LoginRequiredMixin, DetailView):
    model = Accessory
    context_object_name = 'accessory'
    template_name = 'webapp/view_accessory_detail.html'

class AccessoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Accessory
    fields = '__all__'
    context_object_name = 'accessory'
    template_name = 'webapp/view_accessory_confirm_delete.html'
    success_url = reverse_lazy('view_accessory-list')

class AccessoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Accessory
    context_object_name = 'accessory'
    form_class = AccessoryModelForm
    template_name = 'webapp/input_accessory.html'
    success_url = reverse_lazy('view_accessory-list')

# Views for Location objects
class LocationCreateandDisplayView(LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationModelForm
    template_name = 'webapp/input_and_display_location.html'
    success_url = reverse_lazy('input_and_display_location')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = Location.objects.all()
        context['locations'] = locations
        return context

class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    context_object_name = 'locations'
    template_name = 'webapp/view_location.html'

class LocationDetailView(LoginRequiredMixin, DetailView):
    model = Location
    context_object_name = 'location'
    template_name = 'webapp/view_location_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assets'] = Asset.objects.filter(location=self.get_object())
        return context

class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    fields = '__all__'
    context_object_name = 'location'
    template_name = 'webapp/view_location_confirm_delete.html'
    success_url = reverse_lazy('input_and_display_location')

# class LocationUpdateView(UpdateView):
#     model = Location
#     context_object_name = 'location'
#     form_class = LocationModelForm
#     template_name = 'webapp/input_location.html'
#     success_url = reverse_lazy('view_location-list')

def export_assets(request):
    assets = Asset.objects.all()
    # fields = Asset._meta.get_fields()
    all_fields = [f.name for f in Asset._meta.get_fields()]

    # return HttpResponse(" ".join(all_fields))
    object = BytesIO()

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet["A1"] = "category"
    sheet["B1"] = "manufacturer"
    sheet["C1"] = "name"
    sheet["D1"] = "price"
    sheet["E1"] = "Department"
    sheet["F1"] = "Assigned to"
    sheet["G1"] = "location"
    sheet["H1"] = "purchase_date"
    sheet["I1"] = "processor"
    sheet["J1"] = "RAM"
    sheet["K1"] = "HDD"
    sheet["L1"] = "SSD"
    sheet["M1"] = "Checkout status"
    sheet["N1"] = "Status"
    sheet["O1"] = "supplier"
    sheet["P1"] = "serial"
    sheet["Q1"] = "invoice"
    
    for i in range(len(assets)):
        sheet.cell(row = i+2, column = 1).value = assets[i].category.name
        sheet.cell(row = i+2, column = 2).value = assets[i].manufacturer.name
        sheet.cell(row = i+2, column = 3).value = assets[i].name
        sheet.cell(row = i+2, column = 4).value = assets[i].price
        sheet.cell(row = i+2, column = 5).value = assets[i].department.name
        sheet.cell(row = i+2, column = 6).value = assets[i].assigned_to.name
        sheet.cell(row = i+2, column = 7).value = assets[i].location.name
        sheet.cell(row = i+2, column = 8).value = assets[i].purchase_date
        sheet.cell(row = i+2, column = 9).value = assets[i].processor
        sheet.cell(row = i+2, column = 10).value = assets[i].ram
        sheet.cell(row = i+2, column = 11).value = assets[i].hdd
        sheet.cell(row = i+2, column = 12).value = assets[i].ssd
        sheet.cell(row = i+2, column = 13).value = assets[i].checkout_status
        sheet.cell(row = i+2, column = 14).value = assets[i].status.name
        sheet.cell(row = i+2, column = 15).value = assets[i].supplier.name
        sheet.cell(row = i+2, column = 16).value = assets[i].serial
        sheet.cell(row = i+2, column = 17).value = assets[i].invoice

    workbook.save(object)

    # create a response
    response = HttpResponse(content_type='application/vnd.ms-excel')
    # tell the browser what the file is named
    response['Content-Disposition'] = 'attachment;filename="Exported_assets.xlsx"'
    # put the spreadsheet data into the response
    response.write(object.getvalue())
    # return the response
    return response