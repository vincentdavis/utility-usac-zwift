from django.urls import path

from apps.USACycling.api.views import USACyclingProfileAPI, AssociationsAPI, ZwiftProfileAPI, ExportProfileAPI
from apps.USACycling.views import USACycingProfileView, ZwiftProfileView

urlpatterns= [
    path('USACycling/profile', USACycingProfileView.as_view()),
    path('Zwift/profile', ZwiftProfileView.as_view()),
    # API
    path('USACycling/api/profile', USACyclingProfileAPI.as_view()),
    path('USACycling/api/associations', AssociationsAPI.as_view()),
    path('USACycling/api/export', ExportProfileAPI.as_view()),
    path('zwift/api/profile', ZwiftProfileAPI.as_view())

]