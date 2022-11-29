from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm
    login_url = reverse_lazy('login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        res = super().form_valid(form)
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()

        messages.success(self.request, 'Successfully create a product')

        return res

    def get_success_url(self) -> str:
        return reverse_lazy('products-detail', kwargs={'pk': self.object.id})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    login_url = 'login'
    form_class = ProductForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        res = super().form_valid(form)

        messages.success(self.request, 'Successfully update product')

        return res

    def get_success_url(self) -> str:
        return reverse_lazy('products-detail', kwargs={'pk': self.object.id})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_list.html'
    success_url = reverse_lazy('products')
    login_url = 'login'

    def form_valid(self, form):
        res = super().form_valid(form)
        messages.success(self.request, 'Successfully delete product')
        return res
