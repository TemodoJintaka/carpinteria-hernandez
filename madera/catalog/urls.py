from django.urls import path

from .views import CategoryCreateView
from .views import CategoryDeleteView
from .views import CategoryListView
from .views import CategoryUpdateView
from .views import ExchangeRateCreateView
from .views import ExchangeRateDeleteView
from .views import ExchangeRateListView
from .views import ExchangeRateUpdateView
from .views import ProductCreateView
from .views import ProductDeleteView
from .views import ProductListView
from .views import ProductUpdateView

app_name = "catalog"

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path(
        "categories/create/",
        CategoryCreateView.as_view(),
        name="category_create",
    ),
    path(
        "categories/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("products/", ProductListView.as_view(), name="product_list"),
    path(
        "products/create/",
        ProductCreateView.as_view(),
        name="product_create",
    ),
    path(
        "products/<int:pk>/update/",
        ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "products/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "exchange-rates/",
        ExchangeRateListView.as_view(),
        name="exchange_rate_list",
    ),
    path(
        "exchange-rates/create/",
        ExchangeRateCreateView.as_view(),
        name="exchange_rate_create",
    ),
    path(
        "exchange-rates/<int:pk>/update/",
        ExchangeRateUpdateView.as_view(),
        name="exchange_rate_update",
    ),
    path(
        "exchange-rates/<int:pk>/delete/",
        ExchangeRateDeleteView.as_view(),
        name="exchange_rate_delete",
    ),
]
