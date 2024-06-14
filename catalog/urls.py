from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, product_details
from catalog.views import contacts

app_name = CatalogConfig.name


# app_name = 'catalog'

urlpatterns = [
    path('', products_list, name='products_list'),
    path('product/<int:pk>/', product_details, name='product_details'),
    path('contacts/', contacts, name='contacts')
]
