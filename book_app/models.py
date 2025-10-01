from django.db import models

class Author(models.Model):
    first_name = models.CharField('Имя автора', max_length=20)
    surname = models.CharField("Фамилия", max_length=25)
    birthday = models.DateField("Дата рождения")
    bio = models.TextField("Биография")

    def __str__(self):
        return f"{self.surname} {self.first_name}" 

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["surname"]

class Genre(models.Model): 
    name = models.CharField('Название жанра', max_length=100)
    description = models.TextField('Описание жанра') 

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class User(models.Model):
    first_name = models.CharField('Имя пользователя', max_length=100)
    last_name = models.CharField('Фамилия пользователя', max_length=150)
    email = models.EmailField('Почта')
    phone_number = models.CharField('Номер телефона', max_length=20) 

    def __str__(self):
        return f"{self.email}"
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Order(models.Model):
    order_date = models.DateField('Дата заказа')
    total_amount = models.DecimalField('Общая сумма заказа', max_digits=10, decimal_places=2)  
    status = models.CharField('Статус заказа', max_length=100)
    delivery_address = models.CharField('Адрес доставки', max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=0)  

    def __str__(self):
        return f"Заказ #{self.id} - {self.delivery_address}"  
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Book(models.Model):
    title = models.CharField('Название книги', max_length=500)
    publication_date = models.DateField('Дата выпуска')
    price = models.DecimalField('Цена книги', max_digits=8, decimal_places=2)  
    description = models.TextField('Описание')  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', default=0) 
    genres = models.ManyToManyField(Genre, verbose_name='Жанры') 

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ["title"]

class OrderDetail(models.Model):  
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')  
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга') 
    quantity = models.PositiveIntegerField('Количество', default=1)  
    unit_price = models.DecimalField('Цена за позицию', max_digits=8, decimal_places=2)  

    def __str__(self):
        return f"Детали заказа #{self.order.id}"  

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'