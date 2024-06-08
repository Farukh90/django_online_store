# import os
# from django.core.management import BaseCommand
# from django.db import connection
import os
from django.core.management import BaseCommand
import os
from django.core.management import BaseCommand
from django.db import connection

from ...models import Product, Category
from ...utils import read_JSON_data

category_file_path = os.path.join("catalog", "management", "commands", "data", "category.json")
products_file_path = os.path.join("catalog", "management", "commands", "data", "product.json")


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clean_database()
        self.reset_sequences()
        self.load_categories()
        self.load_products()

    def clean_database(self):
        """Очищаем базу данных"""
        Product.objects.all().delete()
        Category.objects.all().delete()

    def reset_sequences(self):
        """Сбрасываем автоинкрементные значения таблиц"""
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")

    def load_categories(self):
        """Загружаем в БД данные по категориям"""
        category_list = read_JSON_data(category_file_path)
        categories = []
        for category_item in category_list:
            category_fields = category_item["fields"]
            category_obj = Category(id=category_item["pk"], **category_fields)
            categories.append(category_obj)
        Category.objects.bulk_create(categories)

    def load_products(self):
        """Загружаем в БД данные по продуктам"""
        product_list = read_JSON_data(products_file_path)
        products = []
        for product_item in product_list:
            product_fields = product_item["fields"]
            category_id = product_fields["category"]
            category_obj = Category.objects.get(id=category_id)
            product_fields["category"] = category_obj
            product_obj = Product(id=product_item["pk"], **product_fields)
            products.append(product_obj)
        Product.objects.bulk_create(products)