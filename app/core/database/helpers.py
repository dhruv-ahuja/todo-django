import os
from pathlib import Path

from django.utils import timezone

from .context_manager import ContextManager
from core.models import TodoItem

# the path to the local database file
# it is automatically created by django in the project root directory
# and that is where the server starts at, in development atleast
db_path = Path(".") / os.environ["DB_NAME"]


def new_todo(task: str, completed: bool = False) -> TodoItem:
    """
    Adds a new ToDo task to the database.
    """
    query = "INSERT INTO core_todoitem (task, completed, added_at) \
    VALUES (?, ?, ?) RETURNING *;"
    query_args = (task, completed, timezone.now())

    with ContextManager(db_path) as db:
        db.cursor.execute(query, query_args)
        result = db.cursor.fetchone()
        db.connection.commit()

    return result


def get_completed_todos() -> list:
    """
    Fetches all completed ToDos from the database.
    """
    query = "SELECT task FROM core_todoitem WHERE completed IS TRUE ORDER BY\
        datetime(added_at) DESC;"

    with ContextManager(db_path) as db:
        db.cursor.execute(query)
        completed_todos = db.cursor.fetchall()

    completed_todos = [task[0] for task in completed_todos]

    return completed_todos


def get_pending_todos() -> list:
    """
    Fetches all pending ToDos from the database.
    """
    query = "SELECT task FROM core_todoitem WHERE completed IS NOT TRUE ORDER BY\
        datetime(added_at) DESC;"

    with ContextManager(db_path) as db:
        db.cursor.execute(query)
        pending_todos = db.cursor.fetchall()

    pending_todos = [task[0] for task in pending_todos]

    return pending_todos
