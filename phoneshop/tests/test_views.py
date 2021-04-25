from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import tempfile
import datetime

from phoneshop.models import Product, Category

class ProductListViewTest(TestCase):
    @classmethod
    def setUp(cls):
        test_user1 = User.objects.create_user(username='testuser1', passowrd = 'hello123')
        test_user2 = User.objects.create_user(username='testuser2', passowrd = 'hello321')

        test_user1.save()
        test_user2.save()

        test_category = Category.objects.create(
            name="Test Category",
            description="Test Description",
            image=tempfile.NamedTemporaryFile(suffix=".png").name,
            slug="test c_slug",
        )

        test_product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            category=test_category,
            price=800,
            image=tempfile.NamedTemporaryFile(suffix=".png").name,
            stock=7,
            available=True,
            created=datetime.now(),
            updated=datetime.now(),
            slug="test p_slug",
        )

        category_objects_for_all = Category.objects.all()
        test_product.category.set(category_objects_for_all)
        test_product.save()
    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('phoneshop:prod_detail'))
        self.assertRedirects(response, '/accounts/login/?next=/phoneshop/products/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='hello123')
        response = self.client.get(reverse('phoneshop:prod_detail'))

        self.assertEqual(str(response.context['user'], 'testuser1'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'product.html')