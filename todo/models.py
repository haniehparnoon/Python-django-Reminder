from django.db import models
import datetime

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique = True)
    description = models.TextField(default='other')

    def __str__(self) -> str:
        return self.category_name

class Task(models.Model):
    category = models.ManyToManyField('Category')
    title = models.CharField(max_length=30)
    description = models.TextField()
    Priority = models.IntegerField()
    due_date = models.DateTimeField()
    create_time = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



