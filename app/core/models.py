from django.db import models


# Create your models here.
class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    added_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
