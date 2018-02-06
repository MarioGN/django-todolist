from django.db.models.query import QuerySet
from django.test import TestCase
from django.shortcuts import resolve_url as r

from model_mommy import mommy

from django_todolist.core.models import Task


class IndexViewGet(TestCase):

    def setUp(self):
        # deleted tasks
        mommy.make('core.Task', active=False, _quantity=4)
        mommy.make('core.Task', _quantity=6)
        self.resp = self.client.get(r('core:index'))

    def tearDown(self):
        Task.objects.all().delete()

    def test_get(self):
        """Get must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must user 'core/index.html'"""
        self.assertTemplateUsed(self.resp, 'core/index.html')

    def test_has_context_list(self):
        context_list = self.resp.context['task_list']
        self.assertIsInstance(context_list, QuerySet)

    def test_list_filter_active(self):
        context_list = self.resp.context['task_list']
        self.assertEqual(6, context_list.count())
