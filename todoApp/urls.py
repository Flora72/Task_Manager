from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('complete/<int:id>/', views.mark_complete, name='mark_complete'),
    path('incomplete/<int:id>/', views.mark_incomplete, name='incomplete_task'),


]