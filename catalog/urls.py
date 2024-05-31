from django.urls import path
from .apps import CatalogConfig
from .views import home_page
from .views import contacts

app_name = CatalogConfig.name


# app_name = 'catalog'

urlpatterns = [
    path('', home_page, name='index'),
    path('contacts/', contacts, name='contacts')
]
