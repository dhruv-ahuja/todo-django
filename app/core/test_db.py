from django.test import TestCase
from django.utils import timezone

from .models import TodoItem


class TodoItemModelTests(TestCase):
    def test_create_todo_item(self):
        """
        Test the insertion of a new ToDo task into the mock test database.
        """
        t = timezone.now()
        task1 = TodoItem(task="test task 1", added_at=t)
        task2 = TodoItem(task="test task 2", added_at=t, completed=True)

        self.assertIs(task1.task, "test task 1")
        self.assertIs(task1.completed, False)

        self.assertIs(task2.task, "test task 2")
        self.assertIs(task2.completed, True)
