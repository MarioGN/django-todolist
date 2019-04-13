from django.test import TestCase
from django.shortcuts import resolve_url as r

from django_todolist.core.models import Task


class CompleteViewGet(TestCase):

    def setUp(self):
        self.task = Task.objects.create(text='My new task')

    def tearDown(self):
        Task.objects.all().delete()

    def test_complete_view(self):
        count = Task.objects.filter(completed=True).count()
        self.client.get(r('core:complete', pk=self.task.pk))
        self.assertTrue(count+1, Task.objects.filter(completed=True).count())
