from django.test import TestCase

from ..models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.name = 'Django'
        self.data1 = Category.objects.create(name=self.name, slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/filed attributes
        :return:
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertTrue(str(self.data1) == self.name)

    def test_category_model_entry(self):
        """
        Test Category model return
        :return:
        """
        data = self.data1
        self.assertEqual(str(self.data1), self.name)


class TestProductModel(TestCase):

    def setUp(self):
        self.name = 'Django'
        cat = Category.objects.create(name=self.name, slug='django')
        user = User.objects.create_user(username='admin')
        self.title = 'Hello'
        self.prod = Product.objects.create(category=cat, created_by=user, title=self.title, slug='hello', price='20', image='django')

    def test_product_model_entry(self):
        """
        Test Category model data insertion/types/filed attributes
        :return:
        """
        data = self.prod
        self.assertEqual(str(self.prod), self.title)
