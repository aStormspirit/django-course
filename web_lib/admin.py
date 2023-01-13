from django.contrib import admin

from .models import Author, Book, ExtUser, Product, Store

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'page_num']


@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    list_display = ['desc', 'is_logged']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']