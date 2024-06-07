import os
from django.core.management import BaseCommand
from django.db import connection

from ...models import Product, Category
from ...utils import read_JSON_data

category = os.path.join("catalog", "management", "commands", "data", "category.json")
products = os.path.join("catalog", "management", "commands", "data", "product.json")


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clean_database()
        self.load_category()
        self.load_products()

    def clean_database(self):
        """очищаем базу данных"""
        Product.objects.all().delete()
        Category.objects.all().delete()

    def load_category(self):
        """загружаем в БД данные по категориям"""
        category_list = read_JSON_data(category)
        for category_item in category_list:
            category_fields = category_item["fields"]
            Category.objects.create(**category_fields)

    def load_products(self):
        """загружаем в БД данные по продуктам"""
        product_list = read_JSON_data(products)
        for product_item in product_list:
            product_fields = product_item["fields"]
            del product_fields["category"]
            Product.objects.create(**product_fields)
