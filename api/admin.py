from django.contrib import admin
from api.models import Restaurant, Category, Comment, Food, Order
# Register your models here.
customModel = [Restaurant, Category, Comment, Food, Order]  # iterable list
admin.site.register(customModel)