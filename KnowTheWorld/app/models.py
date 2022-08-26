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