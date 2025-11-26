from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
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
        name = request.GET.get('name'),
        price= request.GET.get('price'),
        quantity= request.GET.get('quantity'),
        manufacturer=manufacturer
    )
    item.save()

    return HttpResponse("Товар создан", status=201)