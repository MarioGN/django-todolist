from django.test import TestCase

from django_todolist.core.models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(text='My Task')
        self.text_field = Task._meta.get_field('text')

    def tearDown(self):
        self.task.delete()

    def test_created(self):
        self.assertTrue(Task.objects.exists())

    def test_text_value(self):
        self.assertEqual('My Task', self.task.text)

    def test_text_cant_be_blank(self):
        self.assertFalse(self.text_field.blank)

    def test_text_cant_be_null(self):
        self.assertFalse(self.text_field.null)
