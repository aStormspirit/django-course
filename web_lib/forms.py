from cProfile import label
from django.forms import forms
from django.forms import fields, widgets
from .models import Book
from django import forms

class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label="Author UUID", required=False)

class PostAuthors(forms.Form):
    name = forms.CharField(label="name", max_length=150, required=False)
    age = forms.IntegerField(label="age", required=False)
    email = forms.EmailField(label="email", required=False)

class BookForm(forms.ModelForm):
    title = forms.CharField(label="Name Book", max_length=150, required=False)
    color = forms.CharField(label="Color", max_length=150, required=False)

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            "title": "Название книги",
            "description": "Описание книги",
            "page_num": "Количество страниц",
            "author": "Выберите автора"
        }
        widgets = {"description": widgets.TextInput}