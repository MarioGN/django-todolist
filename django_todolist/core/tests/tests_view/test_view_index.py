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
        self.resp_all = self.client.get(r('core:index_filter', filter='all'))

        self.filter = 'invalid_filter'
        self.resp_invalid_filter = self.client.get(r'core:index_filter', filter=filter)

    def tearDown(self):
        Task.objects.all().delete()

    def test_index_list(self):
        context_list = self.resp_index.context['task_list']
        self.assertEqual(len(context_list), len(self.open_tasks))

    def test_index_filter_completed(self):
        context_list = self.resp_completed.context['task_list']
        self.assertEqual(len(context_list), len(self.completed_tasks))

    def test_index_filter_all(self):
        context_list = self.resp_all.context['task_list']
        self.assertEqual(len(context_list), len(Task.objects.all()))

    def test_count_current_list(self):
        current_count = self.resp_index.context['current_count']
        self.assertEqual(len(self.open_tasks), current_count)

    def test_count_completed_list(self):
        completed_count = self.resp_completed.context['completed_count']
        self.assertEqual(len(self.completed_tasks), completed_count)

    def test_count_all(self):
        all_count = self.resp_all.context['all_count']
        self.assertEqual(len(Task.objects.all()), all_count)

    def test_invalid_filter(self):
        from django_todolist.core.views import filter_is_valid

        self.assertEqual('invalid_filter', self.filter)
        self.assertEqual(False, filter_is_valid(self.resp_invalid_filter))
        self.assertEqual(404, self.resp_invalid_filter.status_code)

    def test_context_list_filter(self):
        from django_todolist.core.views import get_context_list
        
        filter = 'all'
        resp_list =  get_context_list('all')
        self.assertNotEquals(None, resp_list)
