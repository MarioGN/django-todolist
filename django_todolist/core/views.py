from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm


def index(request, filter='current'):

    if not filter_is_valid(filter):
        raise Http404

    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TaskForm()

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
        'form': form,
    }

    return render(request, template_name, context)


def delete_task(request, pk, filter='current'):
    task = get_object_or_404(Task, pk=pk)
    task.active = False
    task.save()

    return redirect('core:index_filter', filter=filter)


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()

    return redirect('core:index')


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
