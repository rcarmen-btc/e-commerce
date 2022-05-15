from django import forms
from django.contrib.auth.models import User

from .models import Category


class CreateProductForm(forms.Form):

    category = forms.ModelChoiceField(queryset=Category.objects.all())
    created_by = forms.ModelChoiceField(queryset=User.objects.all())
    title = forms.CharField()
    author = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    slug = forms.SlugField()
    price = forms.DecimalField()
    in_stock = forms.BooleanField()
    is_active = forms.BooleanField()

