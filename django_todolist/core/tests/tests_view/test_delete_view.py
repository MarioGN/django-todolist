from django.test import TestCase
from django.shortcuts import resolve_url as r

from django_todolist.core.models import Task


class DeleteViewGet(TestCase):

    def setUp(self):
        self.task = Task.objects.create(text='My new task')

    def tearDown(self):
        Task.objects.all().delete()

    def test_delete_view(self):
        count = Task.objects.filter(active=False).count()
        self.client.get(r('core:delete', pk=self.task.pk, filter='current'))
        self.assertTrue(count+1, Task.objects.filter(active=False).count())
