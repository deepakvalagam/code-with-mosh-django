from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set','orderitem_set__product').order_by('-placed_at').all()[:5]
    return render(request, 'hello.html', {'orders': list(queryset)})
