from django.shortcuts import render

# Create your views here.
from madera.catalog.models import Product, Category, ExchangeRate
from django.views.generic import ListView
from django.views.generic.detail import DetailView

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    ordering = ['-created_at']
    paginate_by = 10
    queryset = Product.objects.filter(is_published=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    queryset = Product.objects.filter(is_published=True)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:product_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'
    ordering = ['-created_at']
    paginate_by = 10

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'catalog/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'catalog/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/category_delete.html'
    success_url = reverse_lazy('catalog:category_list')

class ExchangeRateCreateView(CreateView):
    model = ExchangeRate
    template_name = 'catalog/exchange_rate_create.html'
    form_class = ExchangeRateForm
    success_url = reverse_lazy('catalog:exchange_rate_list')

class ExchangeRateUpdateView(UpdateView):
    model = ExchangeRate
    template_name = 'catalog/exchange_rate_update.html'
    form_class = ExchangeRateForm
    success_url = reverse_lazy('catalog:exchange_rate_list')