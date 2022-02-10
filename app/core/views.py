import os
from pathlib import Path

from django.shortcuts import render

from .database.context_manager import ContextManager
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
        # now to fetch all the recent most todos
        todos = helpers.get_recently_added_todos()

        return render(request, "core/index.html", {"todos": todos})

    return render(request, "core/index.html")
