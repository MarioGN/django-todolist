from django.db import models


class Task(models.Model):
    text = models.CharField('Task', max_length=200)
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def complete(self):
        self.completed = True
        self.save()

    def delete_task(self):
        self.active = False
        self.save()

    def __str__(self):
        return self.text
