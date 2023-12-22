# services/urls.py
from django.urls import path
from .views import service_list, service_detail, service_create, service_edit, service_delete

urlpatterns = [
    path('list/', service_list, name='service_list'),
    path('<int:pk>/', service_detail, name='service_detail'),
    path('create/', service_create, name='service_create'),
    path('<int:pk>/edit/', service_edit, name='service_edit'),
    path('<int:pk>/delete/', service_delete, name='service_delete'),
]
