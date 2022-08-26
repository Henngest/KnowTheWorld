from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category_id>/<str:subcategory_id>', views.subcategory, name='subcategory'),
]