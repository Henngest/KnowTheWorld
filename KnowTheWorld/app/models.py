from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=50, primary_key=True)

class Subcategory(models.Model):
    class Meta:
        verbose_name_plural = "subcategories"
    name = models.CharField(max_length=50, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Lesson(models.Model):
    text = models.TextField()
    image = models.CharField(max_length=200)
    lesson_subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)