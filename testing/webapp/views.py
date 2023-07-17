from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from datetime import datetime
from .models import Asset, Employee, Category, Manufacturer, Department, Status
from .forms import AssetModelForm, EmployeeModelForm, CategoryModelForm, ManufacturerModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms

# Create your views here.
def index(request):
    return HttpResponse("<H2>HEY! Welcome to my website! </H2>")

def master_page(request):
    return render(request, 'master.html')

def input_inventory(request):
    return render(request, 'webapp/input_inventory.html')

def input_inventory_form(request):
    if request.method == 'POST':
        form = AssetModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('view_inventory-list'))
        # else:
        #     raise ValidationError(_("Employee name must be unique."))
    else:
        form = AssetModelForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'webapp/input_inventory.html', context)

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

class InventoryListView(ListView):
    model = Asset
    context_object_name = 'inventory'
    template_name = 'webapp/view_inventory.html'

class InventoryDetailView(DetailView):
    model = Asset
    context_object_name = 'asset'
    template_name = 'webapp/view_inventory_detail.html'

class InventoryDeleteView(DeleteView):
    model = Asset
    fields = '__all__'
    context_object_name = 'asset'
    template_name = 'webapp/view_inventory_confirm_delete.html'
    success_url = reverse_lazy('view_inventory-list')

class InventoryUpdateView(UpdateView):
    model = Asset
    context_object_name = 'asset'
    form_class = AssetModelForm
    template_name = 'webapp/input_inventory.html'
    success_url = reverse_lazy('view_inventory-list')

def inventory_checkout(request, pk):
    asset = Asset.objects.get(pk=pk)
    if asset.checkout_status == 'I':
        Asset.objects.filter(pk=pk).update(checkout_status='O')
    else:
        Asset.objects.filter(pk=pk).update(checkout_status='I')
    return HttpResponseRedirect(reverse('view_inventory-list'))

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'webapp/view_employees.html'

class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'webapp/view_employee_detail.html'

class EmployeeDeleteView(DeleteView):
    model = Employee
    fields = '__all__'
    context_object_name = 'employee'
    template_name = 'webapp/view_employee_confirm_delete.html'
    success_url = reverse_lazy('view_employee-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    context_object_name = 'employee'
    form_class = EmployeeModelForm
    template_name = 'webapp/input_employee.html'
    success_url = reverse_lazy('view_employee-list')

def image(request):
    return render(request, 'webapp/image.html')

def time_view(request):
    now = datetime.now()
    time = f"Current time is {now}"
    return HttpResponse(time)

# Views for Category objects
class CategoryListView(ListView):
    model = Category
    fields = '__all__'
    context_object_name = 'categories'
    template_name = 'webapp/view_categories.html'

class CategoryDetailView(DetailView):
    model = Category
    fields = '__all__'
    context_object_name = 'category'
    template_name = 'webapp/view_category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'webapp/input_category.html'
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_category-list')

def category_delete(request, pk):
    Category.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_category-list'))

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'webapp/input_category.html'
    success_url = reverse_lazy('view_category-list')

# Views for Manufacturer objects
class ManufacturerListView(ListView):
    model = Manufacturer
    fields = '__all__'
    context_object_name = 'manufacturers'
    template_name = 'webapp/view_manufacturers.html'

class ManufacturerDetailView(DetailView):
    model = Manufacturer
    fields = '__all__'
    context_object_name = 'manufacturer'
    template_name = 'webapp/view_manufacturer_detail.html'

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerModelForm
    template_name = 'webapp/input_manufacturer.html'
    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse_lazy('view_manufacturer-list')

def manufacturer_delete(request, pk):
    Manufacturer.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_manufacturer-list'))

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerModelForm
    template_name = 'webapp/input_manufacturer.html'
    success_url = reverse_lazy('view_manufacturer-list')