from django.contrib import admin

# Register your models here.


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', '')