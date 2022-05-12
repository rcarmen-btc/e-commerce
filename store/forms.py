from django import forms
from django.contrib.auth.models import User

from .models import Category


class CreateForm(forms.Form):

    category = forms.ModelChoiceField(queryset=Category.objects.all())
    created_by = forms.ModelChoiceField(queryset=User.objects.all())
    title = forms.CharField()
    author = forms.CharField()
    description = forms.Textarea(blank=True)
    image = forms.ImageField()
    slug = forms.SlugField()
    price = forms.DecimalField()
    in_stock = forms.BooleanField(default=True)
    is_active = forms.BooleanField(default=True)
