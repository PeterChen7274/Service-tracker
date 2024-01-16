# taskapp/urls.py
from django.urls import path
from .views import task_list, create_task, delete_task, edit_task, extend_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('extend/<int:pk>/', extend_task, name='extend_task'),
]
