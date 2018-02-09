from django.test import TestCase
from django.shortcuts import resolve_url as r

from django_todolist.core.models import Task
from django_todolist.core.forms import TaskEditForm


class EditTaskViewPost(TestCase):

    def setUp(self):
        self.task = Task.objects.create(text='My new task')
        self.new_text = "New description."
        self.data = dict(id_field=self.task.pk, text=self.new_text)

    def tearDown(self):
        Task.objects.all().delete()

    def test_edit_view(self):
        self.assertEqual('My new task', Task.objects.all()[0].text)
        self.client.post(r('core:edit'), self.data)
        self.assertEqual(self.new_text, Task.objects.all()[0].text)
