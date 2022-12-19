from django.urls import path
from .views import pendingList, DetailTask, CreateTask, EditTask
from .views import DeleteTask, login
from django.contrib.auth.views import LogoutView

urlpatterns = [path('',pendingList.as_view(), name='pendings'),
                path('login',login.as_view(), name='login'),
                path('logout',LogoutView.as_view(next_page='login'), name='logout'),
                path('task/<int:pk>',DetailTask.as_view(), name='task'),
                path('create_task/',CreateTask.as_view(), name='create_task'),
                path('edit_task/<int:pk>',EditTask.as_view(), name='edit_task'),
                path('delete_task/<int:pk>',DeleteTask.as_view(), name='delete_task')]
