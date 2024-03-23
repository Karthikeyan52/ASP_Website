from django.urls import path, include
from . import views

urlpatterns = [
    path('read/', views.read, name='read'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
