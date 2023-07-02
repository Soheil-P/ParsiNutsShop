from django.urls import path
from .views import IndexPageView,AboutUsPageView,ContactUsPageView
urlpatterns = [
    path('',IndexPageView.as_view(),name='index-page'),
    path('about-us/',AboutUsPageView.as_view(),name='aboutus-page'),
    path('contact-us/',ContactUsPageView.as_view(),name='contactus-page')
]
