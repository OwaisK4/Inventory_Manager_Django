from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_page, name='dashboard'),
    path('input_inventory/', views.input_inventory_form, name='input_inventory'),
    path('view_inventory/', views.InventoryListView.as_view(), name='view_inventory-list'),
    path('view_inventory/<int:pk>', views.InventoryDetailView.as_view(), name='view_inventory-detail'),
    path('view_inventory/<int:pk>/delete/', views.InventoryDelete.as_view(), name='view_inventory-delete'),
    path('view_inventory/<int:pk>/update/', views.InventoryUpdate.as_view(), name='view_inventory-update'),
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