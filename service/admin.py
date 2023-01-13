from django.contrib import admin

from .models import Product, Bin, Home
# Register your models here.
admin.site.register(Bin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'cost']
    fields = ['id', 'title', 'cost']
    list_filter = ['cost']
    search_fields = ['title']


@admin.register(Home)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['size', 'cost', 'adr', 'bal']