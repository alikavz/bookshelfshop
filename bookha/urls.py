from .views import Booklis, bookdetail, Creating, Updateview, Deleting
from django.urls import path, include


urlpatterns = [
    path('', Booklis.as_view(), name='booklis'),
    path('<int:pk>/', bookdetail, name='detail'),
    path('create/', Creating.as_view(), name='create'),
    path('<int:pk>/update/', Updateview.as_view(), name='up_to_date'),
    path('<int:pk>/delete/', Deleting.as_view(), name='deleting'),
]
