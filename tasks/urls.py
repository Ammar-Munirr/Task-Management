from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("task-create/", views.TaskCreate, name="task-create"),
    path("task-detail/<int:pk>/", views.TaskUpdate, name="task-update"),
    path("task-list/", views.TaskList, name="task-list"),
    path("task-delete/<int:pk>/", views.DeleteTask, name="task-delete"),
    path("get-csv/", views.export_tasks_to_csv, name="get-csv"),
    path("get-json/", views.export_tasks_to_json, name="get-json"),
]
