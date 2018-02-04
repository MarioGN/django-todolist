from django.shortcuts import render

from .models import Task


def index(request):
    task_list = Task.objects.all()
    template_name = 'core/index.html'

    return render(request, template_name, {'task_list': task_list})
