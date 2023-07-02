from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexPageView(TemplateView):
    template_name = "index.html"


class AboutUsPageView(TemplateView):
    template_name = "about.html"


class ContactUsPageView(TemplateView):
    template_name = "contact.html"
