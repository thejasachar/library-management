from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('borrow/', views.borrow_book_view, name='borrow_book'),
    path('return/', views.return_book_view, name='return_book'),
    path('admin/', views.admin_books, name='admin_books'),
]