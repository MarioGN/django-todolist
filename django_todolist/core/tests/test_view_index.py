from django.test import TestCase
from django.shortcuts import resolve_url as r


class IndexViewGet(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('core:index'))

    def test_get(self):
        """Get must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must user 'core/index.html'"""
        self.assertTemplateUsed(self.resp, 'core/index.html')
