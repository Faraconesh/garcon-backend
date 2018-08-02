from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Food(models.Model):
    name = models.CharField(verbose_name=_('Food name'), max_length=100)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=3)
    details = models.CharField(verbose_name=_('Details'), max_length=500)


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
 

class Order(models.Model):
    user = models.ForeignKey(User, related_name=_('User'), on_delete=models.CASCADE)
    food = models.ManyToManyField(to=Food, related_name=_('Food'))
    submitDateTime = models.DateTimeField(verbose_name=_('Submit date time'), auto_now_add=True)
    orderDateTime  = models.DateTimeField(verbose_name=_('Order date time'), auto_now_add=True)
    details = models.CharField(verbose_name=_('Details'),  max_length=500)

    # def __str__(self):
    #     return self.name

    # def __unicode__(self):
    #     return self.name
    