from django.urls import path

from apps.USACycling.api.views import USACyclingProfileAPI
from apps.USACycling.views import USACycingProfileView

urlpatterns= [
    path('profile', USACycingProfileView.as_view()),
    # API
    path('api/profile', USACyclingProfileAPI.as_view())

]