from django.shortcuts import render
from .models import *
# Create your views here.

from django.db.models import Sum, F


def hello(request):
    result = (
        Publication_house
        .objects
        .annotate(
            book_count = models.Count('book')
        ).order_by('name')
    )

    return render(request, 'books.html', {'books':result})