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

    def test_list_filter_active_completed(self):
        context_list = self.resp.context['task_list']
        self.assertEqual(6, context_list.count())


class IndexViewFilters(TestCase):

    def setUp(self):
        self.open_tasks = mommy.make('core.Task', _quantity=3)
        self.completed_tasks = mommy.make(
            'core.Task', completed=True, _quantity=5
        )
        # deleted
        mommy.make('core.Task', active=False, _quantity=2)
        self.resp_index = self.client.get(r('core:index_filter', filter='current'))
        self.resp_completed = self.client.get(r('core:index_filter', filter='completed'))

    def tearDown(self):
        Task.objects.all().delete()

    def test_index_list(self):
        context_list = self.resp_index.context['task_list']
        self.assertEqual(len(context_list), len(self.open_tasks))

    def test_index_filter_completed(self):
        context_list = self.resp_completed.context['task_list']
        self.assertEqual(len(context_list), len(self.completed_tasks))

    def test_index_filter_all(self):
        resp = self.client.get(r('core:index_filter', filter='all'))
        context_list = resp.context['task_list']
        self.assertEqual(len(context_list), len(Task.objects.all()))

    def test_count_current_list(self):
        current_count = self.resp_index.context['current_count']
        self.assertEqual(len(self.open_tasks), current_count)

    def test_count_completed_list(self):
        completed_count = self.resp_completed.context['completed_count']
        self.assertEqual(len(self.completed_tasks), completed_count)
