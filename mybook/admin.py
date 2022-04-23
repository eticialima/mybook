from django.contrib import admin
from mybook.models import Book, BookFiles

# Register your models here.
admin.site.register(Book)
admin.site.register(BookFiles)