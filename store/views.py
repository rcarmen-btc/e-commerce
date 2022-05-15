from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Product, Category
from .forms import CreateProductForm


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


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'store/signup.html'
    success_url = '/accounts/login'


class ProductCreate(LoginRequiredMixin, CreateView):
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


def add_good(req):

    if req.method == 'POST':
        form = CreateProductForm(req.POST, req.FILES)
        if form.is_valid():
            category = form.cleaned_data.get('category')
            created_by = form.cleaned_data.get('created_by')
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            slug = form.cleaned_data.get('slug')
            price = form.cleaned_data.get('price')
            in_stock = form.cleaned_data.get('in_stock')
            is_active = form.cleaned_data.get('is_active')
            obj = Product.objects.create(
                category=category,
                created_by=created_by,
                title=title,
                author=author,
                description=description,
                image=image,
                slug=slug,
                price=price,
                in_stock=in_stock,
                is_active=is_active,
            )
            return HttpResponseRedirect(reverse('store:product_list'))
        else:
            print('Hello')
    else:
        form = CreateProductForm()

    return render(req, 'store/product_create.html', {'form': form})


class UpdateProduct(UpdateView):
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
    template_name = 'store/product_update.html'
    success_url = reverse_lazy('store:product_list')

    def get_context_data(self, **kwargs):
        cntx = super(UpdateProduct, self).get_context_data(**kwargs)
        cntx['slug'] = self.kwargs['slug']
        return cntx


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('store:product_list')
    template_name = 'store/product_delete.html'

    def get_context_data(self, **kwargs):
        cntx = super(DeleteProduct, self).get_context_data(**kwargs)
        cntx['slug'] = self.kwargs['slug']
        return cntx


