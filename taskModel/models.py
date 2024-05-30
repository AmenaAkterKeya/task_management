from django.db import models

from taskCategory.models import TaskCategory
class TaskModel(models.Model):
    taskTittle=models.CharField(max_length=100)
    taskDescription=models.TextField()
    is_completed=models.BooleanField(default=False)
    taskDate= models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(TaskCategory)
    def __str__(self) -> str:
        return self.taskTittle