from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.

# from django.db.models import Sum, F


# def hello(request):
#     result = (
#         Publication_house
#         .objects
#         .annotate(
#             book_count = models.Count('book')
#         ).order_by('name')
#     )

#     return render(request, 'books.html', {'books':result})

# def get_all_items(request):
#     manufacturer = get_object_or_404(
#         Manufacturer,
#         name='Рога и копыта'
#     )
#     item = Item(
#         name = request.GET.get('name'),
#         price= request.GET.get('price'),
#         quantity= request.GET.get('quantity'),
#         manufacturer=manufacturer
#     )
#     item.save()

#     return HttpResponse("Товар создан", status=201)



from django.shortcuts import render

def calculator(request):
    result = None
    opr = ''
    if request.method == 'POST':
        a = float(request.POST.get('num1'))
        b = float(request.POST.get('num2'))
        opr = request.POST.get('operation')
        
        if opr == '+':
            result = a + b
        elif opr == '-':
            result = a - b
        elif opr == '*':
            result = a * b
        elif opr == '/':
            if b != 0:
                result = a / b
            else:
                result = 'Ошибка: деление на ноль'

    return render(request, 'index.html', {'num1': result, 'num2': '', 'result': result, 'operation': opr})
