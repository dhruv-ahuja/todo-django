from audioop import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class UserLoginView(LoginView):
    template_name = "core/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy("tasks")


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "core/home.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        # getting the context from the parent view
        context = super().get_context_data(**kwargs)
        # updating the tasks context to only fetch the posts for the current
        # logged in user
        # since by default, we are fetching all the posts in the db
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        # get the no. of pending tasks
        context["count"] = context["tasks"].filter(completed=False).count()
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
