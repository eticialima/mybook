import os
from django.conf import settings
from django.db import models
from django.utils import timezone

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    
    def __str__(self):
        return "{} - ({})".format(self.first_name, self.last_name) 

class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    pub_data = models.DateField()  
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - ({})".format(self.title, self.pub_data) 


class BookFiles(models.Model):
    book = models.ForeignKey(Book, related_name="files", on_delete=models.CASCADE)
    created_file = models.FileField('Files', upload_to='bookfiles')

    def __str__(self):
        return "{}".format(self.book)  
 