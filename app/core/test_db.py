from django.test import TestCase
from django.utils import timezone

from .database.context_manager import ContextManager
from .database.helpers import db_path


class HelpersTest(TestCase):
    def test_create_todo_item(self):
        """
        Test the insertion of a new ToDo task into the database.
        """
        query = "INSERT INTO core_todoitem (task, added_at, completed) VALUES \
        (?,?,?) RETURNING *;"
        t = timezone.now()
        query_args = ("test task 1", t, False)

        with ContextManager(db_path) as db:
            db.cursor.execute(query, query_args)
            result = db.cursor.fetchone()

        self.assertEqual("test task 1", result[1])
        self.assertEqual(False, result[3])

        query_args = ("test task 2", t, True)

        with ContextManager(db_path) as db:
            db.cursor.execute(query, query_args)
            result = db.cursor.fetchone()

        self.assertEqual("test task 2", result[1])
        self.assertEqual(True, result[3])
