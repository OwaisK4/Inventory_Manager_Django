"""
URL configuration for testing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LogoutView, logout_then_login
from django.urls import path, include, reverse_lazy
from webapp.views import register, UserListView, master_page, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', master_page, name="home"),
    path('about/', about, name="about"),
]

urlpatterns += [
    path('webapp/', include('webapp.urls')),
    path('locallibrary/', include('locallibrary.urls')),
]

urlpatterns += [
    path("accounts/logout/", LogoutView.as_view(next_page=reverse_lazy('login')), name="logout"),
    path("accounts/adduser/", register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('accounts/users/', UserListView.as_view(), name='user-list'),
    # path('accounts/users/<int:pk>', , name='user-detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)