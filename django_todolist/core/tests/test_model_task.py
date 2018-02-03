from django.test import TestCase

from django_todolist.core.models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(text='My Task')

    def tearDown(self):
        self.task.delete()

    def test_created(self):
        self.assertTrue(Task.objects.exists())
