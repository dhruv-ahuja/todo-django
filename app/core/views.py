import django.views.generic as generic
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task


class UserLoginView(LoginView):
    template_name = "core/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


# using FormView since that allows us to setup auto-login after form submission
class UserRegisterView(generic.FormView):
    template_name = "core/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    # if the user is logged in already, then redirect them to the home page
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("tasks")
        return super().get(self, request, *args, **kwargs)

    # auto-login the user after account creation
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class TaskList(LoginRequiredMixin, generic.ListView):
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


class TaskCreate(LoginRequiredMixin, generic.CreateView):
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
class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ["description", "completed"]
    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
