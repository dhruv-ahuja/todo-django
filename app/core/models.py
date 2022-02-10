from django.db import models


# Create your models here.
class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    added_at = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task: {self.task}\nCompleted: {self.completed}"

    class Meta:
        indexes = [
            models.Index(fields=["completed", "added_at"]),
            models.Index(fields=["added_at"]),
        ]
