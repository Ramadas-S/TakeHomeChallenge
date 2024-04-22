from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    unique_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Todo(models.Model):
    unique_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    description = models.TextField()
    completion_status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.description[:50] + "..."
