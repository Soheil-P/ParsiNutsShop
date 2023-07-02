from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,CreateView

from .models import City

# Create your views here.

class AdminDashboardView(TemplateView):
    template_name = "panelbase.html"

class CityListView(ListView):
    model = City
    template_name = "citylist.html"
    context_object_name="cities"

class CityUpdateView(UpdateView):
    model = City
    template_name = "cityedit.html"
    fields="__all__"
    success_url = reverse_lazy('city-list-page')


class CityDeleteView(DeleteView):
    model = City
    template_name = "citydelete.html"
    success_url = reverse_lazy('city-list-page')


class CityCreateView(CreateView):
    model = City
    template_name = "cityadd.html"
    fields='__all__'    
    success_url = reverse_lazy('city-list-page')

