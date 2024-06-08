from django.db import models

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", **NULLABLE
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта", **NULLABLE
    )
    photo = models.ImageField(
        upload_to="catalog/photo",
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
        **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        related_name="products",
        **NULLABLE
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Введите стоимость продукта", **NULLABLE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

    def __str__(self):
        return f'{self.name} {self.price} {self.category}'
