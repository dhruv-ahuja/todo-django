from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task


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
