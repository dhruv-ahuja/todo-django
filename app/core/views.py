import os
from pathlib import Path

from django.shortcuts import render, redirect

from .database import helpers

# the path to the local database file
# it is automatically created by django in the project root directory
# and that is where the server starts at, in development atleast
db_path = Path(".") / os.environ["DB_NAME"]


def index(request):
    if request.method == "POST":
        # we retrieve the task to save to the db
        task = request.POST.get("task")
        # we then pass it onto the helper func that'll save it to the database
        helpers.new_todo(task)

        return redirect("index")

    # we redirect the user back to the index page after form submission
    # in general, we will be fetching the data by default rather than the prev.
    # approach where we were fetching it only after a post request
    # that meant that the page was nothing more than a form in eyes of the
    # browser from what I understand
    completed_todos = helpers.get_completed_todos()
    pending_todos = helpers.get_pending_todos()
    todos = True

    if len(completed_todos) == 0 and len(pending_todos) == 0:
        todos = False

    return render(
        request,
        "core/index.html",
        {
            "completed_todos": completed_todos,
            "pending_todos": pending_todos,
            "todos": todos,
        },
    )


def complete_todo(request, pk):
    helpers.mark_todo_as_completed(pk)
    return redirect("index")


def confirm_deletion(request, pk):
    return render(request, "core/confirm_deletion.html", {"pk": pk})


def delete_todo(request, pk):
    helpers.delete_todo(pk)

    return redirect("index")
