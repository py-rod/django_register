from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sign_up/", views.signup, name="signup"),
    path("login/", views.loginsession, name="login"),
    path("logout/", views.closession, name="logout"),
    path("task/", views.task, name="task"),
    path("task/create/", views.CreateTask, name="createtask"),
    path("task/<int:task_id>/", views.task_detail, name="taskdetail"),
    path("task/<int:task_id>/complete", views.task_complete, name="taskcomplete"),
    path("task/<int:task_id>/delete/", views.task_delete, name="taskdelete"),
]
