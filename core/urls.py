"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('kvp/',views.kvp,name='kvp'),
    path('product/',views.product,name='product'),
    path('product/ui/',views.product_ui,name='product'),
    path('product/ia/',views.product_ia,name='product'),
    path('product/interactions/',views.product_interactions,name='product'),
    path('product/iterations/',views.iterations,name='product'),
    path('product/business-model/',views.business_model,name='product')
]