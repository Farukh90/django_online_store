from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import  ProductDetailView, ProductListView, ProductCreateView
from catalog.views import ContactView

app_name = CatalogConfig.name


# app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('contacts/', ContactView.as_view(), name='contacts')
]

