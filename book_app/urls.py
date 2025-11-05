from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('book/<int:book_id>/', views.book_detail, name='main2'),
]