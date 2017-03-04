from unittest import TestCase

from persistlayer import PersistLayer
from repository import Repository


class TestPersist(TestCase):
    def test_shouldNotInstantiateAbstractClass(self):
        self.assertRaises(TypeError, PersistLayer)

    def test_shouldInstantiateConcreteClass(self):
        testRepo = Repository()

        self.assertIsNotNone(testRepo, 'Test repo is None')
        self.assertIsInstance(testRepo, Repository)


