from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_page, name='dashboard'),
    path('input_inventory/', views.input_inventory_form, name='input_inventory'),
    path('view_inventory/', views.InventoryListView.as_view(), name='view_inventory-list'),
    path('view_inventory/<int:pk>', views.InventoryDetailView.as_view(), name='view_inventory-detail'),
    path('view_inventory/<int:pk>/delete/', views.InventoryDeleteView.as_view(), name='view_inventory-delete'),
    path('view_inventory/<int:pk>/update/', views.InventoryUpdateView.as_view(), name='view_inventory-update'),
    path('view_inventory/<int:pk>/check/', views.inventory_checkout, name='view_inventory-check'),
    path('index/', views.index, name='index'),
    path('time/', views.time_view),
    path('image/', views.image),
]

urlpatterns += [
    path('input_employee/', views.input_employee_form, name='input_employee'),
    path('view_employees/', views.EmployeeListView.as_view(), name='view_employee-list'),
    path('view_employees/<int:pk>', views.EmployeeDetailView.as_view(), name='view_employee-detail'),
    path('view_employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='view_employee-delete'),
    path('view_employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='view_employee-update'),
]

urlpatterns += [
    path('input_category/', views.CategoryCreateView.as_view(), name='input_category'),
    path('view_categories/', views.CategoryListView.as_view(), name='view_category-list'),
    path('view_categories/<int:pk>', views.CategoryDetailView.as_view(), name='view_category-detail'),
    path('view_categories/<int:pk>/delete/', views.category_delete, name='view_category-delete'),
    path('view_categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='view_category-update'),
]

urlpatterns += [
    path('input_manufacturer/', views.ManufacturerCreateView.as_view(), name='input_manufacturer'),
    path('view_manufacturers/', views.ManufacturerListView.as_view(), name='view_manufacturer-list'),
    path('view_manufacturers/<int:pk>', views.ManufacturerDetailView.as_view(), name='view_manufacturer-detail'),
    path('view_manufacturers/<int:pk>/delete/', views.manufacturer_delete, name='view_manufacturer-delete'),
    path('view_manufacturers/<int:pk>/update/', views.ManufacturerUpdateView.as_view(), name='view_manufacturer-update'),
]