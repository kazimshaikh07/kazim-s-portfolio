"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.my_portfolio, name='my_portfolio')
Class-based views
    1. Add an import:  from other_app.views import my_portfolio
    2. Add a URL to urlpatterns:  path('', my_portfolio.as_view(), name='my_portfolio')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from my_portfolio import views

admin.site.site_header = "Kazim Portfolio"
admin.site.site_title = "MOHAMMED KAZIM SHAIKH Admin Portal"
admin.site.index_title = "Welcome to KAZIM's portfolio"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.my_portfolio, name='my_portfolio'),
]
