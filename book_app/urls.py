from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('book/<int:book_id>/', views.book_detail, name='main2'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
]