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
    todos = helpers.get_recently_added_todos()

    return render(request, "core/index.html", {"todos": todos})
