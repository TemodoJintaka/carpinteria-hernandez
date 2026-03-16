from django.shortcuts import render

# Create your views here.
from madera.ventas.models import Lead, Sale
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.db.models import Sum
from django.urls import reverse_lazy
from madera.ventas.models import SaleStatus
from madera.ventas.forms.salesform import SaleForm
from madera.ventas.forms.leadform import LeadForm

class LeadListView(ListView):
    model = Lead
    template_name = 'ventas/lead_list.html'
    context_object_name = 'leads'
    ordering = ['-created_at']
    paginate_by = 10

class LeadDetailView(DetailView):
    model = Lead
    template_name = 'ventas/lead_detail.html'
    context_object_name = 'lead'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    queryset = Lead.objects.all()

class LeadCreateView(CreateView):
    model = Lead
    template_name = 'ventas/lead_create.html'
    form_class = LeadForm
    success_url = reverse_lazy('ventas:lead_list')

class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'ventas/lead_update.html'
    form_class = LeadForm
    success_url = reverse_lazy('ventas:lead_list')

class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'ventas/lead_delete.html'
    success_url = reverse_lazy('ventas:lead_list')


class SaleListView(ListView):
    model = Sale
    template_name = 'ventas/sale_list.html'
    context_object_name = 'sales'
    ordering = ['-created_at']
    paginate_by = 10

class SaleCreateView(CreateView):
    model = Sale
    template_name = 'ventas/sale_create.html'
    form_class = SaleForm
    success_url = reverse_lazy('ventas:sale_list')

class SaleUpdateView(UpdateView):
    model = Sale
    template_name = 'ventas/sale_update.html'
    form_class = SaleForm
    success_url = reverse_lazy('ventas:sale_list')



def sales_report(request):
    hoy = timezone.now()
    # 1. Ganancias totales del mes actual
    ganancia_mes = Sale.objects.filter                        (
        created_at__month=hoy.month,
        status=SaleStatus.CONFIRMED # O 'confirmed'
    ).aggregate(total_mes=Sum('total'))['total_mes'] or 0

    # 2. Producto más vendido
    top_producto = Sale.objects.values('product__name').annotate(
        total_vendido=Sum('quantity')
    ).order_by('-total_vendido').first()

    # 3. Cantidad de pedidos pendientes
    pendientes = Sale.objects.filter(status=SaleStatus.PENDING).count()

    context = {
        'ganancia_mes': ganancia_mes,
        'top_producto': top_producto,
        'pendientes': pendientes,
    }
    return render(request, 'sales/report.html', context)