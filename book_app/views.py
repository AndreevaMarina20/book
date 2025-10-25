from django.shortcuts import render
from .models import Book

def main_page(request):
    books = Book.objects.all()
    
    context = {'books': books}
    return render(request, 'main1.html', context)