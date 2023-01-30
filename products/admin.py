from django.contrib import admin

from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['product', 'author', 'stars', 'active', 'recommend', ]
