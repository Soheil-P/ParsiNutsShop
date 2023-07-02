from django.urls import path
from .views import AdminDashboardView,CityListView,CityUpdateView,CityDeleteView,CityCreateView
urlpatterns = [
    path('',AdminDashboardView.as_view(),name='admin-dashboard-page'),
    path('cities',CityListView.as_view(),name='city-list-page'),
    path('city/edit/<int:pk>/',CityUpdateView.as_view(),name="city-edit-page"),
    path('city/add/',CityCreateView.as_view(),name="city-add-page"),
    path('city/delete/<int:pk>/',CityDeleteView.as_view(),name="city-delete-page"),
]
