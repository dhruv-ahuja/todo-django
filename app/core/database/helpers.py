import os
from pathlib import Path

from django.utils import timezone

from .context_manager import ContextManager


# the path to the local database file
# it is automatically created by django in the project root directory
# and that is where the server starts at, in development atleast
db_path = Path(".") / os.environ["DB_NAME"]


def new_todo(task: str, completed: bool = False):
    """
    Adds a new ToDo task to the database.
    """
    query = "INSERT INTO core_todoitem (task, added_at, completed) \
    VALUES (?, ?, ?) RETURNING *;"
    query_args = (task, timezone.now(), completed)

    with ContextManager(db_path) as db:
        db.cursor.execute(query, query_args)
        result = db.cursor.fetchone()
        db.connection.commit()

    return result


def new_todo_test(task: str, completed: bool = False):
    """
    Adds a new ToDo task to the database.
    """
    db_path = "./app/db.sqlite3"
    query = "INSERT INTO core_todoitem (task, added_at, completed) \
    VALUES (?, ?, ?) RETURNING *;"
    import datetime

    query_args = (task, datetime.datetime.now(), completed)

    with ContextManager(db_path) as db:
        db.cursor.execute(query, query_args)
        result = db.cursor.fetchone()
        db.connection.commit()

    return result
