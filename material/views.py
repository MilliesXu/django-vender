from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView
)
from django.urls import reverse_lazy

from .forms import MaterialForm
from .models import Material


# Create your views here.
class MaterialListView(ListView):
    model = Material
    template_name = 'material/material_list.html'


class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material/material_create.html'
    success_url = reverse_lazy('materials')
    login_url = reverse_lazy('login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        res = super().form_valid(form)
        material = form.save(commit=False)
        material.user = self.request.user
        material.save()

        messages.success(self.request, 'Successfully create material')

        return res


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'material/material_detail.html'


class MaterialUpdateView(LoginRequiredMixin, UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material/material_update.html'
    success_url = reverse_lazy('materials')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        res = super().form_valid(form)

        messages.success(self.request, 'Successfully update material')

        return res

    def get_success_url(self) -> str:
        return reverse_lazy(
                'materials-detail',
                kwargs={'pk': self.object.id}
            )


class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = Material
    template_name = 'material/material_list.html'
    success_url = reverse_lazy('materials')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(self.request, 'Successfully delete material')
        return res
