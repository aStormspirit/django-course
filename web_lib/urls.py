from django.urls import path
from web_lib import views

urlpatterns = [
    path('', views.main, name='web_lib'),
    path('authors',views.authors, name='authors'),
    path('books', views.books, name='books'),
    path('about', views.about, name='about'),
    path('author_id/<uuid:pk>', views.author_id, name='author_id'),
    path('create_book', views.create_book, name='create_book')

]
