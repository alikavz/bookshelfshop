from .views import Booklis
from django.urls import path, include


urlpatterns = [
    path('admin/', Booklis.as_view(), name='booklis'),
    ]
