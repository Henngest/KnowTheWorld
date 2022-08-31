from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    class Meta:
        verbose_name_plural = "subcategories"

    name = models.CharField(max_length=50, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    text = models.TextField()
    image = models.CharField(max_length=200)
    lesson_subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return "Lesson"


class Quiz(models.Model):
    quiz_level = models.IntegerField()
    quiz_subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return "Quiz "+self.quiz_level.__str__()


class Question(models.Model):
    image = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    is_correct_choice = models.BooleanField(default=False)
    choice_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text