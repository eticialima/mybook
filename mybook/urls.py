from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.AuthorList.as_view(), name='author-list'),
    path('author-create/', views.AuthorCreate.as_view(), name='author-add'), 
    
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'), 
    path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),  
    
    
    
    path('book-list/<int:pk>', views.BookList.as_view(), name='book-list'),
    path('book/add/<int:pk>', views.BookFilesCreate.as_view(), name='book-add'), 
    path('book-update/<int:pk>', views.BookFilesUpdate.as_view(), name='book-update'),
    path('book-delete/<int:pk>', views.BookDelete.as_view(), name='book-delete'),
] 
