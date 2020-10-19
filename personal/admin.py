from django.contrib import admin
from .models import Post, Comment, Customer

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_on', 'status')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')


@admin.register(Customer)
class CusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'message']
