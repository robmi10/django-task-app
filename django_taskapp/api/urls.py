from django.urls import path
from .views import TaskView, TaskItemView, UserView
from . import views

urlpatterns = [
    path('task', views.create_task, name= "create-task"),
    path('task-update', views.update_task_status, name= "update-task"),
    path('task-delete', views.delete_task, name= "delete-task"),

    path('taskitem', views.post_taskitem, name= "post-taskitem"),
    path('taskitem-update', views.update_taskitem, name= "update-taskitem"),
    path('taskitem-delete', views.delete_taskitem, name= "delete-taskitem"),

    path('create-user', views.create_user, name= "user-create"),
    path('login-user', views.login_user, name= "user-login"),
]
