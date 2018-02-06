from django.shortcuts import render

from .models import Task


def index(request, filter='current'):

    if filter == 'current':
        task_list = Task.objects.filter(active=True).filter(completed=False)

    template_name = 'core/index.html'

    return render(request, template_name, {'task_list': task_list})
