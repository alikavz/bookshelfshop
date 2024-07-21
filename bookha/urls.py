from .views import Booklis, Bookdetail, Creating
from django.urls import path, include


urlpatterns = [
    path('', Booklis.as_view(), name='booklis'),
    path('<int:pk>/', Bookdetail.as_view(), name='detail'),
    path('create/', Creating.as_view(), name='create'),
]
