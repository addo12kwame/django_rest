"""
URL configuration for drinks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns

from drinks.views import drink_list, drink_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', drink_list),
    path('drinks/<int:id>/', drink_detail),
]
# Helps you get json format like a normal view without the rest_framework html page when we make api call
# This is done by adding ".json" to the endpoint
# But we have to change our view signatures to take an additional format argument
urlpatterns = format_suffix_patterns(urlpatterns)
