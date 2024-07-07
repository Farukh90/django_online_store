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
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        related_name="products",
        **NULLABLE,
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Введите стоимость продукта", **NULLABLE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="versions",
        verbose_name="product",
    )
    version_number = models.CharField(max_length=50, verbose_name="Номер версии")
    version_name = models.CharField(max_length=150, verbose_name="Название версии")
    is_current = models.BooleanField(
        default=False, verbose_name="Признак текущей версия"
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продукта"
        ordering = ["product"]

    def __str__(self):
        return f"{self.product.name} - {self.version_name} ({self.version_number})"
