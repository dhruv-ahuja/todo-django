from django.urls import path

from .views import *


urlpatterns = [
    path("", TodoList.as_view(), name="todos"),
    path("create", TodoCreate.as_view(), name="create_task"),
    path("update/<int:pk>", TodoUpdate.as_view(), name="update_task"),
]
