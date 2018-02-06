from django.http import Http404
from django.shortcuts import render

from .models import Task


def index(request, filter='current'):
    task_list = []
    template_name = 'core/index.html'
    active_button = 'current'


    if filter == 'current':
        task_list = Task.objects.filter(active=True).filter(completed=False)
    elif filter == 'completed':
        active_button = 'completed'
        task_list = Task.objects.filter(active=True).filter(completed=True)
    elif filter == 'all':
        active_button = 'all'
        task_list = Task.objects.all()
    else:
        raise Http404

    return render(request, template_name, context)
