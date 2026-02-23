from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('read/<int:id>/', views.mark_as_read, name='mark_read'),
    path('delete/<int:id>/', views.delete_message, name='delete_message'),
]