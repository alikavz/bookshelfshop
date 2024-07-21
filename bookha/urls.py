from .views import Booklis, Bookdetail
from django.urls import path, include


urlpatterns = [
    path('', Booklis.as_view(), name='booklis'),
    path('<int:pk>/', Bookdetail.as_view(), name='detail'),
]
