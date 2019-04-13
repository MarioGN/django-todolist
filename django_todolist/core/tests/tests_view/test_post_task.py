from django.test import TestCase
from django.shortcuts import resolve_url as r

from django_todolist.core.models import Task
from django_todolist.core.forms import TaskForm


class PostTaskForm(TestCase):

    def setUp(self):
        self.count = Task.objects.all().count()
        self.data = dict(text='My new task')

    def tearDown(self):
        Task.objects.all().delete()

    def test_post_create_index(self):
        self.client.post(r('core:index'), self.data)
        self.assertEqual(self.count+1, Task.objects.all().count())

    def test_post_create_index_filter(self):
        self.client.post(r('core:index_filter', filter='current'), self.data)
        self.assertEqual(self.count+1, Task.objects.all().count())

        self.client.post(r('core:index_filter', filter='completed'), self.data)
        self.assertEqual(self.count+2, Task.objects.all().count())

        self.client.post(r('core:index_filter', filter='all'), self.data)
        self.assertEqual(self.count+3, Task.objects.all().count())
