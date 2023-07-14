from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from datetime import datetime
from .models import Asset, Employee
from .forms import AssetModelForm, EmployeeModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
            return HttpResponseRedirect(reverse('view_employee-list'))
    else:
        form = EmployeeModelForm(request.POST)
    context = {
        'form': form,
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

class InventoryDelete(DeleteView):
    model = Asset
    fields = '__all__'
    context_object_name = 'asset'
    template_name = 'webapp/view_inventory_confirm_delete.html'
    success_url = reverse_lazy('view_inventory-list')

class InventoryUpdate(UpdateView):
    model = Asset
    context_object_name = 'asset'
    form_class = AssetModelForm
    template_name = 'webapp/input_inventory.html'
    success_url = reverse_lazy('view_inventory-list')

def inventory_checkout(request, pk):
    asset = Asset.objects.get(pk=pk)
    if asset.status == 'I':
        Asset.objects.filter(pk=pk).update(status='O')
    else:
        Asset.objects.filter(pk=pk).update(status='I')
    return HttpResponseRedirect(reverse('view_inventory-list'))

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'webapp/view_employees.html'

class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'webapp/view_employee_detail.html'

class EmployeeDelete(DeleteView):
    model = Employee
    fields = '__all__'
    context_object_name = 'employee'
    template_name = 'webapp/view_employee_confirm_delete.html'
    success_url = reverse_lazy('view_employee-list')

class EmployeeUpdate(UpdateView):
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