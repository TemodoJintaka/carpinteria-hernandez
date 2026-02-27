from django.shortcuts import render

# Create your views here.
from madera.catalog.models import Product, Category, ExchangeRate
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .CategoryForm import CategoryForm
from .ProductForm import ProductForm
from .ExchangerateForm import ExchangeRateForm

class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category/lista.html'
    context_object_name = 'categories'
    ordering = ['name']
    paginate_by = 10


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'catalog/category/crear.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'catalog/category/editar.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/category/eliminar.html'
    success_url = reverse_lazy('catalog:category_list')



class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product/lista.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product/crear.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/product/editar.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product/eliminar.html'
    success_url = reverse_lazy('catalog:product_list')

class ExchangeRateListView(ListView):
    model = ExchangeRate
    template_name = 'catalog/exchange/lista.html'
    context_object_name = 'exchange_rates'
    paginate_by = 10

class ExchangeRateCreateView(CreateView):
    model = ExchangeRate
    template_name = 'catalog/exchange/crear.html'
    form_class = ExchangeRateForm
    success_url = reverse_lazy('catalog:exchange_rate_list')

class ExchangeRateUpdateView(UpdateView):
    model = ExchangeRate
    template_name = 'catalog/exchange/editar.html'
    form_class = ExchangeRateForm
    success_url = reverse_lazy('catalog:exchange_rate_list')

class ExchangeRateDeleteView(DeleteView):
    model = ExchangeRate
    template_name = 'catalog/exchange/eliminar.html'
    success_url = reverse_lazy('catalog:exchange_rate_list')