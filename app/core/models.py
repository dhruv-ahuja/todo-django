from django.db import models


# Create your models here.
class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    added_at = models.DateTimeField()

    def __str__(self):
        return self.task

    class Meta:
        indexes = [
            models.Index(fields=["completed", "added_at"]),
            models.Index(fields=["added_at"]),
        ]

        # ordering = ["completed"]
