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
    queryset = Product.objects.all().order_by('-unit_price','title')[:5]
    return render(request, 'hello.html', {'products': list(queryset)})
