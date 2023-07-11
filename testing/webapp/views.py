from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from datetime import datetime
from .models import Asset
from .forms import AssetModelForm

# Create your views here.
def index(request):
    return HttpResponse("<H2>HEY! Welcome to my website! </H2>")

def master_page(request):
    return render(request, 'master.html')

def input_inventory(request):
    return render(request, 'webapp/input_inventory.html')

def input_inventory_form(request):
    if request.method == 'POST':
        form = AssetModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = AssetModelForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'webapp/input_inventory.html', context)

class InventoryListView(ListView):
    model = Asset
    context_object_name = 'inventory'
    template_name = 'webapp/view_inventory.html'

class AssetListLiew(ListView):
    model = Asset
    # paginate_by = 10
    context_object_name = 'asset_list'
    template_name = 'webapp/asset_list.html'
    def get_queryset(self):
        return Asset.objects.all()

class AssetDetailView(DetailView):
    model = Asset
    template_name = 'webapp/asset_detail.html'

class AssetCreate(CreateView):
    model = Asset
    fields = '__all__'

class AssetUpdate(UpdateView):
    model = Asset
    fields = '__all__'

class AssetDelete(DeleteView):
    model = Asset
    fields = '__all__'
    success_url = reverse_lazy('assets')


def image(request):
    return render(request, 'webapp/image.html')

def time_view(request):
    now = datetime.now()
    time = f"Current time is {now}"
    return HttpResponse(time)
