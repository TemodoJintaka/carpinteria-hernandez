# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from madera.catalog.models import Category
from madera.catalog.models import ExchangeRate
from madera.catalog.models import Product

from .Forms.CategoryForm import CategoryForm
from .Forms.ExchangerateForm import ExchangeRateForm
from .Forms.ProductForm import ProductForm


# Vista para la página de inicio
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "pages/home.html"


# Vistas para Categorías
# CategoryListView: Muestra la lista paginada de categorías.
# CategoryCreateView: Permite crear una nueva categoría usando un formulario.
# CategoryUpdateView: Permite editar una categoría existente.
# CategoryDeleteView: Permite eliminar una categoría seleccionada.


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "catalog/category/lista.html"
    context_object_name = "categories"
    ordering = ["name"]
    paginate_by = 10


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "catalog/category/crear.html"
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "catalog/category/editar.html"
    form_class = CategoryForm
    success_url = reverse_lazy("catalog:category_list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "catalog/category/eliminar.html"
    success_url = reverse_lazy("catalog:category_list")


# Vistas para Productos
# ProductListView: Muestra la lista paginada de productos.
# ProductCreateView: Permite crear un nuevo producto usando un formulario.
# ProductUpdateView: Permite editar un producto existente.
# ProductDeleteView: Permite eliminar un producto seleccionado.


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/product/lista.html"
    context_object_name = "products"
    paginate_by = 10


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "catalog/product/crear.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "catalog/product/editar.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product/eliminar.html"
    success_url = reverse_lazy("catalog:product_list")


# Vistas para Tasas de cambio
# ExchangeRateListView: Muestra la lista paginada de tasas de cambio.
# ExchangeRateCreateView: Permite crear una nueva tasa de cambio usando un formulario.
# ExchangeRateUpdateView: Permite editar una tasa de cambio existente.
# ExchangeRateDeleteView: Permite eliminar una tasa de cambio seleccionada.


class ExchangeRateListView(LoginRequiredMixin, ListView):
    model = ExchangeRate
    template_name = "catalog/exchange/lista.html"
    context_object_name = "exchange_rates"
    paginate_by = 10


class ExchangeRateCreateView(LoginRequiredMixin, CreateView):
    model = ExchangeRate
    template_name = "catalog/exchange/crear.html"
    form_class = ExchangeRateForm
    success_url = reverse_lazy("catalog:exchange_rate_list")


class ExchangeRateUpdateView(LoginRequiredMixin, UpdateView):
    model = ExchangeRate
    template_name = "catalog/exchange/editar.html"
    form_class = ExchangeRateForm
    success_url = reverse_lazy("catalog:exchange_rate_list")


class ExchangeRateDeleteView(LoginRequiredMixin, DeleteView):
    model = ExchangeRate
    template_name = "catalog/exchange/eliminar.html"
    success_url = reverse_lazy("catalog:exchange_rate_list")
