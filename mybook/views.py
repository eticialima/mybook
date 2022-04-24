from django.utils import timezone
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView 
from .forms import AuthorForm, BookFilesFormSet, BookForm
from .models import Author, Book


class AuthorList(ListView):
    template_name = 'author_list.html'
    form_class = AuthorForm
    model = Author
    context_object_name = 'author_list' 

class AuthorCreate(CreateView):
    template_name = 'author_create.html'
    model = Author
    form_class = AuthorForm 
    success_url = reverse_lazy('author-list') 
    
class AuthorUpdate(UpdateView):
    template_name = 'author_create.html'
    form_class = AuthorForm
    model = Author
    success_url = reverse_lazy('author-list') 

class AuthorDelete(DeleteView):
    template_name = 'author_delete.html' 
    model = Author
    success_url = reverse_lazy('author-list') 
    
    

class BookList(ListView):
    template_name = 'book_list.html'
    model = Book
    form_class = BookForm
    
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = {
            'pk': kwargs['pk'],
            'author_book': Book.objects.filter(author_id=self.kwargs.get('pk')),
            'author': Author.objects.filter(pk=self.kwargs.get('pk'))
        }
        return self.render_to_response(context)
    
    def get_queryset(self): 
        return self.model.objects.filter(author_id=self.kwargs['pk'])
 
class BookFilesCreate(CreateView):
    model = Book
    template_name = 'book_create.html' 
    form_class = BookForm 
    
    def get_context_data(self, **kwargs):
        data = super(BookFilesCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['bookfiles'] = BookFilesFormSet(self.request.POST, self.request.FILES)
        else:
            data['bookfiles'] = BookFilesFormSet()
        return data

    def form_valid(self, form): 
        author = Author.objects.filter(pk=self.kwargs.get('pk')) 
        context = self.get_context_data()
        form = self.get_form()
        bookfiles = context['bookfiles']
        with transaction.atomic():
            form_model = form.save(commit=False) 
            form_model.author = author[0] 
            self.object = form.save() 
            if bookfiles.is_valid(): 
                bookfiles.instance = self.object 
                bookfiles.save()
        return super(BookFilesCreate, self).form_valid(form)
    
    def get_success_url(self): 
        return reverse_lazy('book-list', kwargs={'pk': self.object.author.id})


class BookFilesUpdate(UpdateView):
    model = Book
    template_name = 'book_create.html' 
    form_class = BookForm 

    def get_context_data(self, **kwargs):
        data = super(BookFilesUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['bookfiles'] = BookFilesFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['bookfiles'] = BookFilesFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        bookfiles = context['bookfiles']
        with transaction.atomic():
            self.object = form.save()

            if bookfiles.is_valid():
                bookfiles.instance = self.object
                bookfiles.save()
        return super(BookFilesUpdate, self).form_valid(form)
    
    def get_success_url(self): 
        return reverse_lazy('book-list', kwargs={'pk': self.object.author.id})
    
class BookDelete(DeleteView):
    model = Book
    template_name = 'book_delete.html'  
    
    def get_success_url(self): 
        return reverse_lazy('book-list', kwargs={'pk': self.object.author.id})
    