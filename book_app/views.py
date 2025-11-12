from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Book

def main_page(request):
    # Получаем параметры поиска и фильтрации
    search_query = request.GET.get('search', '')
    selected_category = request.GET.get('category')
    
    # Начинаем с всех книг
    books = Book.objects.all()
    
    # Применяем поиск если есть запрос
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__first_name__icontains=search_query) |
            Q(author__surname__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Применяем фильтр по категории если выбрана
    if selected_category:
        books = books.filter(category=selected_category)
    
    # Получаем все доступные категории
    categories = Book.ST
    
    context = {
        'books': books,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query
    }
    return render(request, 'main1.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    context = {'book': book}
    return render(request, 'main2.html', context)

def cart(request):
    cart_items = []
    total_price = 0 
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_count': len(cart_items)
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, book_id):
    return redirect('cart')