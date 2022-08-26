from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Subcategory

def index(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {'categories': categories}
    return render(request,'app/index.html', context)