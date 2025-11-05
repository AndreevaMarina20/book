from django.db import models

class Author(models.Model):
    first_name = models.CharField('Имя автора', max_length=20)
    birthday = models.DateField(null=True, blank=True)
    surname = models.CharField("Фамилия", max_length=25)
    bio = models.TextField("Биография")

    def __str__(self):
        return f"{self.first_name} {self.surname}" 

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
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Order(models.Model):
    ST=[
        ("Собран","Собран"),
        ("Собираем","Собираем"),
        ("Курьер в пути","Курьер в пути"),
        ("Доставлен","Достален")
    ]

    order_date = models.DateField('Дата заказа')
    total_amount = models.DecimalField('Общая сумма заказа', max_digits=10, decimal_places=2)  
    status = models.CharField('Статус заказа', max_length=100, choices=ST)
    delivery_address = models.CharField('Адрес доставки', max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=0) 
    order_detail = models.ManyToManyField('OrderDetail', verbose_name='Детали заказа', related_name='order_relation') 

    def __str__(self):
        return f"Заказ #{self.id} - {self.user}"  
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Book(models.Model):
    ST=[
        ("Художественная литература","Художественная литература"),
        ("Фантастика","Фантастика"),
        ("Детективы","Детективы"),
        ("Романы","Романы")
    ]

    title = models.CharField('Название книги', max_length=500)
    publication_date = models.DateField('Дата выпуска')
    price = models.DecimalField('Цена книги', max_digits=8, decimal_places=2)  
    description = models.TextField('Описание')  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', default=0) 
    genres = models.ManyToManyField(Genre, verbose_name='Жанры') 
    category = models.CharField('Категории', max_length=100, choices=ST)
    photo = models.ImageField(upload_to='books/', blank=True, null=True)

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
        return f"Детали заказа #{self.order.id} {self.order}"  

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'