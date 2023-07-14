from django.urls import path
from . import views

urlpatterns = [
    path('', views.master_page, name='dashboard'),
    path('input_inventory/', views.input_inventory_form, name='input_inventory'),
    path('view_inventory/', views.InventoryListView.as_view(), name='view_inventory-list'),
    path('view_inventory/<int:pk>', views.InventoryDetailView.as_view(), name='view_inventory-detail'),
    path('view_inventory/<int:pk>/delete/', views.InventoryDelete.as_view(), name='view_inventory-delete'),
    path('view_inventory/<int:pk>/update/', views.InventoryUpdate.as_view(), name='view_inventory-update'),
    path('view_inventory/<int:pk>/check/', views.inventory_checkout, name='view_inventory-check'),
    path('index/', views.index, name='index'),
    path('time/', views.time_view),
    path('image/', views.image),
]

urlpatterns += [
    path('input_employee/', views.input_employee_form, name='input_employee'),
    path('view_employees/', views.EmployeeListView.as_view(), name='view_employee-list'),
    path('view_employees/<int:pk>', views.EmployeeDetailView.as_view(), name='view_employee-detail'),
    path('view_employees/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='view_employee-delete'),
    path('view_employees/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='view_employee-update'),
]