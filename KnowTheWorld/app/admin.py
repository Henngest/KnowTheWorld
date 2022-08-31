from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizResults)