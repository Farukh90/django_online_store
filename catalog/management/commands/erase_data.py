import os
from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Product, Category
from catalog.utils import read_JSON_data

category_file_path = os.path.join(
    "catalog", "management", "commands", "data", "category.json"
)
products_file_path = os.path.join(
    "catalog", "management", "commands", "data", "product.json"
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clean_database()
        self.reset_sequences()

    def clean_database(self):
        """Очищаем базу данных"""
        Product.objects.all().delete()
        Category.objects.all().delete()

    def reset_sequences(self):
        """Сбрасываем автоинкрементные значения таблиц"""
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")
