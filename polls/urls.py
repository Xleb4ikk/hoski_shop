from django.urls import path
from .views import home
from . import views
from polls.models import Sock
import os
import django

# Удаляем все записи
Sock.objects.all().delete()

# Получаем все записи
socks = Sock.objects.all()
print(f"Количество товаров: {socks.count()}")

# Выводим все товары
for sock in socks:
    print(sock.name, sock.price)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noski_shop.settings')
django.setup()

# Добавляем уникальные записи
Sock.objects.create(name='Красные носки', description='Удобные красные носки', price=199.99, stock=10)
Sock.objects.create(name='Синие носки', description='Стильные синие носки', price=249.99, stock=5)
Sock.objects.create(name='Зеленые носки', description='Зеленые носки с узором', price=299.99, stock=8)

print("База данных заполнена!")

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
]
