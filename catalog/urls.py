from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home_page
from catalog.views import contacts

app_name = CatalogConfig.name


# app_name = 'catalog'

urlpatterns = [
    path('', home_page, name='index'),
    path('contacts/', contacts, name='contacts')
]
