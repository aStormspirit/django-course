from django.shortcuts import render, redirect
from web_lib.models import Author, Book

from .forms import SearchAuthor, PostAuthors, BookForm
from django.forms import modelform_factory

# Create your views here.
def main(req):
    book_form = BookForm()
    return render(req, "web_lib/main.html", {"form": book_form})


def create_book(req):
    book_form = BookForm()
    if req.method == "POST":
        book_form = BookForm(req.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.description = book_form.cleaned_data['description'] + ' ' + book_form.cleaned_data['color']
            book.save()
            book_form.save_m2m()
            return redirect('books')
    return render(req, "web_lib/book_form.html", {"form": book_form})


#    book_form = modelform_factory(
#    Book, 
#    fields= ['title', 'description'],
#    help_texts={"title": "Enter title"}
#     )
#    form = SearchAuthor(req.GET)
#    form_post = PostAuthors(req.POST)
#    return render(req, 'web_lib/main.html', {"form": form, "form_post": form_post})

def authors(req):
    if "author_uuid" in req.GET:
        return redirect("author_id", req.GET["author_uuid"])

    if req.method == "POST":
        data = dict()
        data["name"] = req.POST.get('name')
        data["age"] = req.POST.get('age')
        data["email"] = req.POST.get('email')
        Author.objects.create(**data)


    all_authors = {'authors': Author.objects.all()}
    return render(req, 'web_lib/authors.html', all_authors)

def author_id(req, pk):
    author = Author.objects.get(pk=pk)
    books_amount = author.book_set.count()
    found_author = {'author': author, 'books_amount': books_amount}
    return render(req, 'web_lib/author_id.html', found_author)

def books(req):
    all_books = {'books': Book.objects.all()}
    return render(req, 'web_lib/books.html', all_books)


def about(req):
    return render(req, 'web_lib/about.html')