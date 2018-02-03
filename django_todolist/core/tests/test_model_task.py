from django.test import TestCase

from django_todolist.core.models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(text='My Task')

    def tearDown(self):
        self.task.delete()

    def test_created(self):
        self.assertTrue(Task.objects.exists())

    def test_text_value(self):
        self.assertEqual('My Task', self.task.text)

    def test_text_blank(self):
        field = Task._meta.get_field('text')
        self.assertFalse(field.blank)

    def test_text_null(self):
        field = Task._meta.get_field('text')
        self.assertFalse(field.null)
