from django.contrib import admin

from .models import Genre, Publisher, Autor, Book, User

admin.site.register(User)

admin.site.register(Genre)


admin.site.register(Publisher)

admin.site.register(Autor)

admin.site.register(Book)


# Register your models here.
