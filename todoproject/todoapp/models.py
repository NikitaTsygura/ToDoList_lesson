from django.db import models

# Create your models here.


class ToDoListItem(models.Model):
    content = models.TextField()