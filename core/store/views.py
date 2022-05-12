from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView

from .models import Product, Category


class ProductList(ListView):
    model = Product

    def get_queryset(self):
        if self.kwargs.get('slug', 0):
            return Product.objects.filter(category__slug=self.kwargs['slug'])
        return Product.objects.all()

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('slug', 0):
            context['curr_category'] = self.kwargs['slug']
        context['categories'] = Category.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product


class ProductCreate(CreateView):
    model = Product
    fields = [
        'title',
        'category',
        'created_by',
        'author',
        'image',
        'description',
        'slug',
        'price',
        'in_stock',
        'is_active'
    ]
    template_name = 'store/product_create.html'


