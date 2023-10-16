from django.urls import path
from . import views



urlpatterns = [
    path('task-create/',views.TaskCreate,name='task-create'),
    path('task-detail/<int:pk>/',views.TaskUpdate,name='task-update'),
    path('',views.TaskList,name='task-list'),
    path('task-delete/<int:pk>/',views.DeleteTask,name='task-delete')
]
