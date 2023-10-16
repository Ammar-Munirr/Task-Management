from django.urls import path
from . import views



urlpatterns = [
    path('task-create/',views.TaskCreate,name='task-create')
]
