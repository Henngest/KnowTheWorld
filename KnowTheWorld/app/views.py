from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Subcategory, NewUserForm
from django.contrib.auth.decorators import login_required


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'app/index.html', context)


@login_required()
def subcategory(request, category_id, subcategory_id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    subcategory = Subcategory.objects.get(pk=subcategory_id)
    context = {'category': category,
               'subcategory': subcategory,
               'categories': categories}
    return render(request, 'app/subcategory.html', context)


def register_request(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="app/register.html", context={"register_form": form,
                                                                               'categories': categories})


def login_request(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="app/login.html", context={"login_form": form,
                                                                            'categories': categories})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def profile(request):
    categories = Category.objects.all()
    return render(request, template_name="app/profile.html", context={"user": request.user,
                                                                      'categories': categories})