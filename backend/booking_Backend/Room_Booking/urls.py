from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from Room_Booking import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('rooms/', views.RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/', views.RoomDetail.as_view(), name='room-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)