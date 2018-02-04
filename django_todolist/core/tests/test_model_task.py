from django.test import TestCase

from datetime import date

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

    def test_created_at(self):
        self.assertEqual(date.today(), self.task.created_at)

    def test_completed(self):
        self.assertFalse(self.task.completed)

    def test_active(self):
        self.assertTrue(self.task.active)

    def test_str(self):
        self.assertEqual(self.task.text, str(self.task))

    def test_complete_task(self):
        self.assertFalse(self.task.completed)
        self.task.complete()
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        self.assertTrue(self.task.active)
        self.task.delete_task()
        self.assertFalse(self.task.active)
