from django.test import TestCase

from django_todolist.core.forms import TaskForm


class TaskFormTest(TestCase):

    def test_form_has_fields(self):
        """Must have 1 text field"""
        form = TaskForm()
        expected = ['text', ]
        self.assertSequenceEqual(expected, list(form.fields))
