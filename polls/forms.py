from django import forms
from .models import Product

class OrderForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label="Выберите товар")
    quantity = forms.IntegerField(min_value=1, label="Количество") 