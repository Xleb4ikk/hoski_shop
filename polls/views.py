from django.http import HttpResponse

from django.shortcuts import render
from .models import Sock

def home(request):
    socks = Sock.objects.all()  # Получаем все товары из базы
    return render(request, 'polls/home.html', {'socks': socks})

def product_list(request):
    products = Sock.objects.all()  # Используем модель Sock
    return render(request, 'polls/product_list.html', {'products': products})

