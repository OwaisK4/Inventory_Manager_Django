from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_page, name='dashboard'),
    path('input_inventory/', views.input_inventory_form, name='input_inventory'),
    path('view_inventory/', views.InventoryListView.as_view(), name='view_inventory'),
    path('index/', views.index, name='index'),
    path('time/', views.time_view),
    path('image/', views.image),
]

urlpatterns += [
    path('assets/', views.AssetListLiew.as_view(), name='asset-list'),
    path('asset/<int:pk>', views.AssetDetailView.as_view(), name='asset-detail'),
    path('asset/create/', views.AssetCreate.as_view(), name='asset-create'),
    path('asset/<int:pk>/update/', views.AssetUpdate.as_view(), name='asset-update'),
    path('asset/<int:pk>/delete/', views.AssetDelete.as_view(), name='asset-delete'),
]