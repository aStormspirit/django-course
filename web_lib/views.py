from django.shortcuts import render
from web_lib.models import Author, Book
# Create your views here.
def main(req):
    return render(req, 'web_lib/main.html')

def authors(req):
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