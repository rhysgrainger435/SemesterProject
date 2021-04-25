from django.test import TestCase
from phoneshop.models import Category, Product, Comment


class CommentModelTest(TestCase):
    def setUp(self):
        Comment.objects.create(author='Big')

    def test_author_label(self):
        cooment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')
    

    def test_get_absolute_url(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.get_absolute_url(), '/comment/author/1')