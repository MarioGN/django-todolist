from django.test import TestCase

from django_todolist.core.forms import TaskForm


class TaskFormTest(TestCase):

    def test_form_has_fields(self):
        """Must have 1 text field"""
        form = TaskForm()
        expected = ['text', ]
        self.assertSequenceEqual(expected, list(form.fields))

    def test_text_is_required(self):
        """Text field is required"""
        form = self.make_validated_form(text='')
        self.assertTrue(form.errors)
        
        errors = form.errors.as_data()
        errors_list = errors['text']
        exception = errors_list[0]
        self.assertEqual('required', exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(text='My task')
        data = dict(valid, **kwargs)
        form = TaskForm(data)
        form.is_valid()
        return form
