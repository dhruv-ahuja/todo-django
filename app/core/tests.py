from django.test import TestCase
from django.utils import timezone

from .models import Task


class TaskModelTests(TestCase):
    def test_create_tasks(self):
        """
        Test the insertion of a new ToDo task into the mock test database.
        """
        t = timezone.now()
        task1 = Task(description="test task 1", added_at=t)
        task2 = Task(description="test task 2", added_at=t, completed=True)

        self.assertIs(task1.description, "test task 1")
        self.assertIs(task1.completed, False)

        self.assertIs(task2.description, "test task 2")
        self.assertIs(task2.completed, True)
