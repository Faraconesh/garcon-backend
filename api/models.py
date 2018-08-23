from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from datetime import datetime

# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=75, help_text=_('Maximum 75 characters'))
    picture = models.FileField(upload_to='Categories/', blank=True, null=True)
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Restaurant(models.Model):
    name = models.CharField(verbose_name=_('Restaurant name'), max_length=75, help_text=_('Maximum 75 characters'))
    picture = models.FileField(upload_to='Restaurants/', blank=True, null=True)
    menuPicture = models.FileField(upload_to='Restaurants/', blank=True, null=True)
    userWeight = models.PositiveIntegerField(verbose_name=_('User Weight'), default=0, blank=True, null=True)
    customWeight = models.PositiveIntegerField(verbose_name=_('Custom Weight'), default=0, blank=True, null=True)
    # categories = models.ManyToManyField(Category, related_name=_('RestaurantCategory'))
        
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name=_('RestaurantFood'), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Food name'), max_length=75, help_text=_('Maximum 75 characters'))
    picture = models.FileField(upload_to='Foods/', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name=_('Price'))
    categories = models.ManyToManyField(Category, related_name=_('FoodCategory'), blank=True)
    userWeight = models.PositiveIntegerField(verbose_name=_('User Weight'), default=0, blank=True, null=True)
    customWeight = models.PositiveIntegerField(verbose_name=_('Custom Weight'), default=0, blank=True, null=True)
    details = models.TextField(verbose_name=_('Details'),  max_length=1000, help_text=_('Maximum 1000 characters'), blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, related_name=_('UserComments'), on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name=_('FoodComments'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=75, help_text=_('Maximum 75 characters'))
    content = models.TextField(verbose_name=_('Content'), max_length=1000, help_text=_('Maximum 1000 characters'))

    def __str__(self):
        return str(self.user.username) + ' said about ' + str(self.food.name)

    def __unicode__(self):
        return str(self.user.username) + ' said about ' + str(self.food.name)


class Order(models.Model):
    user = models.ForeignKey(User, related_name=_('UserOrder'), on_delete=models.CASCADE)
    food = models.ManyToManyField(Food, related_name=_('Food'))
    status = models.NullBooleanField(verbose_name=_('Status'), default=False, blank=True)
    submitDateTime = models.DateTimeField(verbose_name=_('Submit date time'), auto_now_add=True)
    orderDateTime  = models.DateField(verbose_name=_('Order date time'), default=datetime.today().strftime('%Y-%m-%d'), blank=True)
    details = models.TextField(verbose_name=_('Details'),  max_length=1000, help_text=_('Maximum 1000 characters'), blank=True, null=True)

    def __str__(self):
        return str(self.user.username) + ' ' + str(self.orderDateTime)

    def __unicode__(self):
        return str(self.user.username) + ' ' + str(self.orderDateTime)
