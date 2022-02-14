from django.urls import path

from .views import *


urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("create", TaskCreate.as_view(), name="create_task"),
    path("update/<int:pk>", TaskUpdate.as_view(), name="update_task"),
    path("delete/<int:pk>", TaskDelete.as_view(), name="delete_task"),
]
