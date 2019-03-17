from django.test import TestCase
from .models import Board

# Create your tests here.
class Blog1TestCase(TestCase):
    def setUp(self):
        Board.objects.create(title='hello',pic='')
        Board.objects.create(title='you',pic='')
        Board.objects.create(title='why',pic='')

    def testCount(self):
        return self.assertEqual(Board.objects.all().count(), 1)

    def test1(self):
        return self.assertEqual(Board.objects.get(title='hello').title, 'hello')
