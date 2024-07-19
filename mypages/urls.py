from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import Homepage

urlpatterns = [
    path('home/', Homepage.as_view(), name='home'),
]
