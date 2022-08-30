from django.contrib import admin

from .models import Category, Subcategory, Lesson, Quiz, Question, Choice

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)