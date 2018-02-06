from django.http import Http404
from django.shortcuts import render

from .models import Task


def index(request, filter='current'):
    task_list = []
    template_name = 'core/index.html'
    active_button = 'current'

    current_count = Task.objects.filter(active=True).filter(completed=False).count()
    completed_count = Task.objects.filter(active=True).filter(completed=True).count()
    all_count = Task.objects.all().count()

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

    context = {
        'task_list': task_list,
        'active_button': active_button,
        'current_count': current_count,
        'completed_count': completed_count,
        'all_count': all_count,
    }

    return render(request, template_name, context)
