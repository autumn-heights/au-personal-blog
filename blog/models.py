# blog/models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)  # Creates a VARCHAR field in the database
    content = models.TextField()              # Creates a TEXT field for longer content
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
