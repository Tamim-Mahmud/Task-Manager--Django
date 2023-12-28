from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Tasks_list(models.Model):
    PRIORITY_CHOICES = [
        (3, 'Low'),
        (2, 'Medium'),
        (1, 'High'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='todo_images/', blank=True, null=True)
    due_date = models.DateTimeField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)  # Default to Medium
    is_complete = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.title} {self.description}")