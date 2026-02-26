from django.shortcuts import render

# Create your views here.
from madera.ventas.models import Lead
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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