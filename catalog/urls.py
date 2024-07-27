from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductDetailView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView, ProductDeleteView,
)
from catalog.views import ContactView

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_details"),
    path("product/create", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactView.as_view(), name="contacts"),
]