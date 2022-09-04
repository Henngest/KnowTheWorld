from django.contrib import admin

from .models import *

class ChoiceAdmin(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceAdmin,]

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizResults)