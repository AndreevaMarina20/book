from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Book)
admin.site.register(OrderDetail)