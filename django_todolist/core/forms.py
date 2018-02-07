from django import forms

from .models import Task


class TaskForm(models.ModelForm):

    model = Task
    fields = ('text',)
