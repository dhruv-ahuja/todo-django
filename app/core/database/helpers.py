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


def get_recently_added_todos() -> list:
    """
    Fetches the recent few ToDo tasks from the database.
    """
    query = "SELECT task, completed FROM core_todoitem ORDER BY datetime(added_at) DESC LIMIT 10;"

    with ContextManager(db_path) as db:
        db.cursor.execute(query)
        todos = db.cursor.fetchmany(10)

    return todos
