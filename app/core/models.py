from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        indexes = [
            models.Index(fields=["completed", "added_at"]),
            models.Index(fields=["added_at"]),
        ]

        ordering = ["completed"]
