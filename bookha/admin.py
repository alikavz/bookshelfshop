from django.contrib import admin
from .models import Book, Comment


class Commentadmin(admin.ModelAdmin):
    list_display = ('user', 'Which_book', 'text', 'date')


admin.site.register(Book)
admin.site.register(Comment, Commentadmin)
