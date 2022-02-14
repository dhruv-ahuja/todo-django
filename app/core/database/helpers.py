import os
from pathlib import Path

from django.utils import timezone

from .context_manager import ContextManager
from core.models import Task

# the path to the local database file
# it is automatically created by django in the project root directory
# and that is where the server starts at, in development atleast
db_path = Path(".") / os.environ["DB_NAME"]


def new_todo(task: str, completed: bool = False) -> Task:
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
    query = "SELECT id, task FROM core_todoitem WHERE completed IS TRUE ORDER BY\
        datetime(added_at) DESC;"

    with ContextManager(db_path) as db:
        db.cursor.execute(query)
        completed_todos = db.cursor.fetchall()

    return completed_todos


def get_pending_todos() -> list:
    """
    Fetches all pending ToDos from the database.
    """
    query = "SELECT id, task FROM core_todoitem WHERE completed IS NOT TRUE ORDER BY\
        datetime(added_at) DESC;"

    with ContextManager(db_path) as db:
        db.cursor.execute(query)
        pending_todos = db.cursor.fetchall()

    return pending_todos


def mark_todo_as_completed(pk):
    """
    Marks a pending ToDo as completed and updates the database.
    """
    query = "UPDATE core_todoitem SET completed = TRUE WHERE id = ?;"

    with ContextManager(db_path) as db:
        db.cursor.execute(query, (pk,))
        db.connection.commit()


def mark_todo_as_pending(pk):
    """
    Marks a completed ToDo as pending once again and updates the database.
    """
    query = "UPDATE core_todoitem SET completed = FALSE where id = ?;"

    with ContextManager(db_path) as db:
        db.cursor.execute(query, (id,))
        db.connection.commit()


def delete_todo(pk):
    """
    Deletes a specific ToDo from the database given its ID.
    """
    query = "DELETE FROM core_todoitem WHERE ID =? RETURNING *;"

    with ContextManager(db_path) as db:
        db.cursor.execute(query, (pk,))
        result = db.cursor.fetchone()
        db.connection.commit()

    return result
