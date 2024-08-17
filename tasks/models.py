from django.db import models
from categories.models import Category
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    assigned_at = models.DateTimeField()
    category = models.ManyToManyField(Category)
    
    def __str__(self) -> str:
        return self.title