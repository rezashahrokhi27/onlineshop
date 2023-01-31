from django.contrib import admin

from .models import Product, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'stars', 'active', 'recommend', ]
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [CommentsInline, ]


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['product', 'author', 'stars', 'active', 'recommend', ]
