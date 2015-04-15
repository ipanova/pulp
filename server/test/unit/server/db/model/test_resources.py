"""
This module contains tests for the pulp.server.db.model.resources module.
"""
import unittest

from pulp.server.db.model import resources


class TestReservedResource(unittest.TestCase):

    def test_attributes(self):
        rr = resources.ReservedResource('my-task', 'some-worker', 'some-resource')
        self.assertEqual(rr.task_id, 'my-task')
        self.assertEqual(rr.worker_name, 'some-worker')
        self.assertEqual(rr.resource_id, 'some-resource')
        self.assertFalse('_id' in rr._fields)
        self.assertFalse('id' in rr._fields)

    def test_indixes(self):
        self.assertEqual(resources.ReservedResource._meta['indexes'],
                         ['-worker_name', '-resource_id'])
