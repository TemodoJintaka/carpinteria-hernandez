from django.urls import path
from .views import (
CategoryListView, 
CategoryCreateView, 
CategoryUpdateView, 
CategoryDeleteView, 
ProductListView,
ProductCreateView, 
ProductUpdateView,
)
app_name = 'catalog'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]