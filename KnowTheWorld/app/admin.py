from django.contrib import admin

from .models import Category, Subcategory, Lesson

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Lesson)