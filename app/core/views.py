from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Task


class UserLoginView(LoginView):
    template_name = "core/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    # success_url = reverse_lazy("tasks")

    def get_success_url(self):
        return reverse_lazy("tasks")


class UserRegisterView(CreateView):
    template_name = "core/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


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
    fields = ["description", "completed"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        # this class method is executed when the POSTed form is valid
        # the data is sent to be saved into the DB.
        # we set the user here, having excluded it form the form itself
        # since we don't want user x to be able to post on the behalf of
        # user y.
        form.instance.user = self.request.user
        # and here, we are calling the un-modified form_valid() function defined
        # by the superclass. this is our own modified version, we add the user
        # here and then call the original form_valid() to actually store the
        # task created into the db
        return super().form_valid(form)


# we don't need to modify the form here since the user is already being
# selected when creating a task above.
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["description", "completed"]
    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
