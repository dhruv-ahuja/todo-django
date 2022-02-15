from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


urlpatterns = [
    path("login", UserLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(next_page="login"), name="logout"),
    path("", TaskList.as_view(), name="tasks"),
    path("create", TaskCreate.as_view(), name="create_task"),
    path("update/<int:pk>", TaskUpdate.as_view(), name="update_task"),
    path("delete/<int:pk>", TaskDelete.as_view(), name="delete_task"),
]
