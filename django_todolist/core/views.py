from django.http import Http404
from django.shortcuts import render

from .models import Task


def index(request, filter='current'):
    task_list = []
    template_name = 'core/index.html'

    if filter == 'current':
        task_list = Task.objects.filter(active=True).filter(completed=False)
    elif filter == 'completed':
        task_list = Task.objects.filter(active=True).filter(completed=True)
    elif filter == 'all':
        task_list = Task.objects.all()
    else:
        raise Http404

    return render(request, template_name, {'task_list': task_list})
