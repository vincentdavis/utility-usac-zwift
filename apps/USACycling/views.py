from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class USACycingProfileView(TemplateView):
    template_name = 'USA-Profile.html'


class ZwiftProfileView(TemplateView):
    template_name = 'Zwift-Profile.html'