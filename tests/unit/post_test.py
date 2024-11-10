from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_postcreate(self):
        p=Post('Test','Test Author','Test Content')
        self.assertEqual('Test',p.title)
        self.assertEqual('Test Author',p.author)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p=Post('Test','Test Content')
        expected={'title': 'Test Title', 'author': 'Test Author', 'content': 'Test Content'}
        self.assertDictEqual(expected, p.json())