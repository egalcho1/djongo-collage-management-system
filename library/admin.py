from django.contrib import admin

from library.models import Book, Library

# Register your models here.
admin.site.register(Library)
admin.site.register(Book)