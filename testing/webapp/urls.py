from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('time/', views.time_view),
    path('', views.templatized_index),
    path('myself/', views.myself),
    path('about/', views.about_page),
    path('components/', views.components_page),
    path('image/', views.image),
]