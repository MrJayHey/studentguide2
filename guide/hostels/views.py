from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Hostel



class HostelsListView(ListView):
    model = Hostel
    template_name = "index.html"
    context_object_name = 'hostels'

