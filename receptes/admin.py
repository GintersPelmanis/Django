from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Rating, Ingridient, Recepie, Product, Category 

# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Recepie)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Ingridient)