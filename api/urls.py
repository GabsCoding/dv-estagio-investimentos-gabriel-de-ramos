from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='Overview'),
    path('new-client/', views.create, name='New Client'),
    path('update-client/<str:id>/', views.update, name='Update Client'),
    path('delete-client/<str:id>/', views.delete, name='Delete Client'),
]