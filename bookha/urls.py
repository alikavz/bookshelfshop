from .views import Booklis, Bookdetail, Creating, Updateview
from django.urls import path, include


urlpatterns = [
    path('', Booklis.as_view(), name='booklis'),
    path('<int:pk>/', Bookdetail.as_view(), name='detail'),
    path('create/', Creating.as_view(), name='create'),
    path('<int:pk>/update/', Updateview.as_view(), name='up_to_date'),
]
