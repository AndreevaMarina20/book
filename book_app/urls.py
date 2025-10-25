from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('Главная', views.main_page, name='main_ru'),  # если нужно для русского URL
]