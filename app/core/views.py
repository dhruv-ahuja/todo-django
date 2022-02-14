from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Task


class TodoList(ListView):
    model = Task
    template_name = "core/home.html"
    context_object_name = "todos"


class TodoCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todos")


class TodoUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todos")
