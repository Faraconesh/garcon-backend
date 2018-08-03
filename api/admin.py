from django.contrib import admin
from api.models import Food, Order
# Register your models here.
customModel = [Food, Order]  # iterable list
admin.site.register(customModel)