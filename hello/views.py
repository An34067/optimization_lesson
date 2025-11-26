from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

from django.db.models import Sum, F


# def hello(request):
#     result = (
#         Publication_house
#         .objects
#         .annotate(
#             book_count = models.Count('book')
#         ).order_by('name')
#     )

#     return render(request, 'books.html', {'books':result})

def get_all_items(request):
    manufacturer = get_object_or_404(
        Manufacturer,
        name='Рога и копыта'
    )
    item = Item(
        name = 'проверочный товар',
        price=50.000,
        quantity=1000,
        manufacturer=manufacturer
    )
    item.save()