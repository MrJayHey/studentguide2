"""
URL configuration for guide project.

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
from django.contrib import admin
from django.urls import path, include
from .views import Main
from links.views import LinksView
from hostels.views import HostelsListView
from teachers.views import TeachersView
from rasp.views import RaspView
from RaspAPI.views import RaspGRUPAPIView
from RaspAPI.views import UpdateAPIView
from RaspAPI.views import GRUPAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='main'),
    path('auth/', include('site_auth.urls')),
    path('links/', LinksView.as_view(), name='links'),
    path('hostels/', HostelsListView.as_view(), name='hostels'),
    path('rasp/', RaspView.as_view(), name='rasp'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('api/V1/getRasp/', RaspGRUPAPIView.as_view()),
    path('api/V1/getGroups/', GRUPAPIView.as_view()),
    path('api/V1/Update/', UpdateAPIView.as_view()),
]
