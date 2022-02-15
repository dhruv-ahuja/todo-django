from audioop import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from .models import Task


class UserLoginView(LoginView):
    template_name = "core/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy("tasks")


class UserLogoutView(LogoutView):
    template_name = "core/logout.html"
    fields = "__all__"
    next_page = reverse_lazy("login")


class TaskList(ListView):
    model = Task
    template_name = "core/home.html"
    context_object_name = "tasks"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
