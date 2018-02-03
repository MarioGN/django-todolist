from django.db import models


class Task(models.Model):
    text = models.CharField('Tarefa', max_length=200)
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
