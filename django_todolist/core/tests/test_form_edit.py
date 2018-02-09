from django.test import TestCase

from django_todolist.core.forms import TaskEditForm


class TaskEditFormTest(TestCase):

    def test_form_has_fields(self):
        """Must have 2 fields"""
        form = TaskEditForm()
        expected = ['id_field', 'text']
        self.assertSequenceEqual(expected, list(form.fields))
