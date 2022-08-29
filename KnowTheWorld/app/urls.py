from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category_id>/<str:subcategory_id>', views.subcategory, name='subcategory'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile, name="profile")
]