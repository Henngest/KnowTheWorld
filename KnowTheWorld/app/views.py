from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Subcategory


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'app/index.html', context)

def subcategory(request, category_id, subcategory_id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    subcategory = Subcategory.objects.get(pk=subcategory_id)
    context = {'category': category,
               'subcategory': subcategory,
               'categories': categories}
    return render(request, 'app/subcategory.html', context)
