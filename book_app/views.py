from django.shortcuts import render, get_object_or_404
from .models import Book

def main_page(request):
    books = Book.objects.all()
    
    context = {'books': books}
    return render(request, 'main1.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    context = {'book': book}
    return render(request, 'main2.html', context)