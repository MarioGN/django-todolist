from django.http import Http404
from django.shortcuts import render

from .models import Task


def index(request, filter='current'):

    if not filter_is_valid(filter):
        raise Http404

    template_name = 'core/index.html'

    current_count = get_context_list(filter='current').count()
    completed_count = get_context_list(filter='completed').count()
    all_count = get_context_list(filter='all').count()

    task_list = get_context_list(filter)
    active_button = filter

    context = {
        'task_list': task_list,
        'active_button': active_button,
        'current_count': current_count,
        'completed_count': completed_count,
        'all_count': all_count,
    }

    return render(request, template_name, context)


def get_context_list(filter):

    task_list = None

    if filter == 'current':
        task_list = Task.objects.filter(active=True).filter(completed=False)
    elif filter == 'completed':
        task_list = Task.objects.filter(active=True).filter(completed=True)
    elif filter == 'all':
        task_list = Task.objects.all()

    return task_list


def filter_is_valid(filter):
    if filter != 'current' and filter != 'completed' and filter != 'all':
        return False
    return True
