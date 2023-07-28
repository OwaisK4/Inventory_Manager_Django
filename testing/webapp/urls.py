from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('webhook/', views.webhook, name='webhook'),
    path('activity_log/', views.ActivityListView.as_view(), name='activity_log'),
    path('input_inventory/', views.input_inventory_form, name='input_inventory'),
    path('view_inventory/', views.InventoryListView.as_view(), name='view_inventory-list'),
    path('view_inventory/<int:pk>/', views.InventoryDetailView.as_view(), name='view_inventory-detail'),
    path('view_inventory/<int:pk>/delete/', views.InventoryDeleteView.as_view(), name='view_inventory-delete'),
    path('view_inventory/<int:pk>/update/', views.InventoryUpdateView.as_view(), name='view_inventory-update'),
    path('view_inventory/<int:pk>/barcode/', views.generate_barcode, name='view_inventory-barcode'),
    path('view_inventory/barcodes/', views.generate_all_barcodes, name='view_inventory-all-barcodes'),
    # path('view_inventory/<int:pk>/check/', views.inventory_checkout, name='view_inventory-check'),
    path('index/', views.index, name='index'),
    path('time/', views.time_view),
]

urlpatterns += [
    path('input_accessory/', views.AccessoryCreateView.as_view(), name='input_accessory'),
    path('view_accessories/', views.AccessoryListView.as_view(), name='view_accessory-list'),
    path('view_accessories/<int:pk>/', views.AccessoryDetailView.as_view(), name='view_accessory-detail'),
    path('view_accessories/<int:pk>/delete/', views.AccessoryDeleteView.as_view(), name='view_accessory-delete'),
    path('view_accessories/<int:pk>/update/', views.AccessoryUpdateView.as_view(), name='view_accessory-update'),
]

urlpatterns += [
    path('view_inventory/<int:pk>/attachements/', views.inventory_attachements_list, name='view_inventory-attachements-list'),
    path('view_inventory/<int:pk>/attachements/add', views.InventoryAttachementsAddView.as_view(), name='view_inventory-attachements-add'),
    path('view_inventory/<int:pk>/attachements/<int:pk_attachement>/delete', views.inventory_attachements_delete, name='view_inventory-attachements-delete'),
]

urlpatterns += [
    path('view_inventory/<int:pk>/maintenances/', views.inventory_maintenances_list, name='view_inventory-maintenances-list'),
    path('view_inventory/<int:pk>/maintenances/add/', views.InventoryMaintenancesAddView.as_view(), name='view_inventory-maintenances-add'),
    path('view_inventory/<int:pk>/maintenances/<int:pk_maintenance>/delete/', views.inventory_maintenances_delete, name='view_inventory-maintenances-delete'),
]

urlpatterns += [
    path('view_inventory/<int:pk>/checkout_log/', views.inventory_checkout_list, name='view_inventory-checkout-list'),
    path('view_inventory/<int:pk>/checkout_log/checkout/', views.CheckoutView.as_view(), name='view_inventory-checkout'),
    path('view_inventory/<int:pk>/checkout_log/check-in/', views.CheckinView.as_view(), name='view_inventory-checkin'),
    # path('view_inventory/<int:pk>/checkout_log/<int:pk_checkout>/delete', views.inventory_maintenances_delete, name='view_inventory-checkout-delete'),
]

urlpatterns += [
    path('view_inventory/<int:pk>/audit_log/', views.inventory_audit_list, name='view_inventory-audit-list'),
    path('view_inventory/<int:pk>/audit_log/audit/', views.InventoryAuditView.as_view(), name='view_inventory-audit'),
    path('view_inventory/<int:pk>/audit_log/audit_schedule/', views.InventoryAuditScheduleView.as_view(), name='view_inventory-audit-schedule'),
    path('view_inventory/scheduled_audits/', views.ScheduledAuditsListView.as_view(), name='view_inventory-scheduled-audit-list'),
    path('view_inventory/scheduled_audits/<int:pk>/', views.scheduled_audit_view, name='view_inventory-scheduled-audit'),
]

urlpatterns += [
    path('input_employee/', views.input_employee_form, name='input_employee'),
    path('view_employees/', views.EmployeeListView.as_view(), name='view_employee-list'),
    # path('view_employees/<int:pk>', views.EmployeeDetailView.as_view(), name='view_employee-detail'),
    path('view_employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='view_employee-delete'),
    path('view_employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='view_employee-update'),
]

urlpatterns += [
    path('input_category/', views.CategoryCreateView.as_view(), name='input_category'),
    path('view_categories/', views.CategoryListView.as_view(), name='view_category-list'),
    # path('view_categories/<int:pk>', views.CategoryDetailView.as_view(), name='view_category-detail'),
    path('view_categories/<int:pk>/delete/', views.category_delete, name='view_category-delete'),
    path('view_categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='view_category-update'),
]

urlpatterns += [
    path('input_manufacturer/', views.ManufacturerCreateView.as_view(), name='input_manufacturer'),
    path('view_manufacturers/', views.ManufacturerListView.as_view(), name='view_manufacturer-list'),
    # path('view_manufacturers/<int:pk>', views.ManufacturerDetailView.as_view(), name='view_manufacturer-detail'),
    path('view_manufacturers/<int:pk>/delete/', views.manufacturer_delete, name='view_manufacturer-delete'),
    path('view_manufacturers/<int:pk>/update/', views.ManufacturerUpdateView.as_view(), name='view_manufacturer-update'),
]

urlpatterns += [
    path('input_supplier/', views.SupplierCreateView.as_view(), name='input_supplier'),
    path('view_suppliers/', views.SupplierListView.as_view(), name='view_supplier-list'),
    # path('view_suppliers/<int:pk>', views.SupplierDetailView.as_view(), name='view_supplier-detail'),
    path('view_suppliers/<int:pk>/delete/', views.supplier_delete, name='view_supplier-delete'),
    path('view_suppliers/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='view_supplier-update'),
]

urlpatterns += [
    path('input_department/', views.DepartmentCreateView.as_view(), name='input_department'),
    path('view_departments/', views.DepartmentListView.as_view(), name='view_department-list'),
    # path('view_departments/<int:pk>', views.DepartmentDetailView.as_view(), name='view_department-detail'),
    path('view_departments/<int:pk>/delete/', views.department_delete, name='view_department-delete'),
    path('view_departments/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='view_department-update'),
]

urlpatterns += [
    path('input_status/', views.StatusCreateView.as_view(), name='input_status'),
    path('view_statuses/', views.StatusListView.as_view(), name='view_status-list'),
    # path('view_statuses/<int:pk>', views.StatusDetailView.as_view(), name='view_status-detail'),
    path('view_statuses/<int:pk>/delete/', views.status_delete, name='view_status-delete'),
    path('view_statuses/<int:pk>/update/', views.StatusUpdateView.as_view(), name='view_status-update'),
]

urlpatterns += [
    path('input_location/', views.LocationCreateandDisplayView.as_view(), name='input_and_display_location'),
    path('view_locations/', views.LocationListView.as_view(), name='view_location-list'),
    path('view_locations/<int:pk>/', views.LocationDetailView.as_view(), name='view_location-detail'),
    path('view_locations/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='view_location-delete'),
]

urlpatterns += [
    path('export/assets/', views.export_assets, name='export_assets'),
    path('export/accessories/', views.export_accessories, name='export_accessories'),
    path('export/employees/', views.export_employees, name='export_employees'),
    path('export/categories/', views.export_categories, name='export_categories'),
    path('export/manufacturers/', views.export_manufacturers, name='export_manufacturers'),
    path('export/suppliers/', views.export_suppliers, name='export_suppliers'),
    path('export/departments/', views.export_departments, name='export_departments'),
]