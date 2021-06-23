from django.db import models
from mongoengine import DynamicDocument, fields
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

class PizzaSize(DynamicDocument):
    size = fields.StringField(max_length=30,unique=True,required=True)

class PizzaTopping(DynamicDocument):
    topping = fields.StringField(max_length=40,unique=True,required=True)

PIZZA_TYPE_CHOICE = [
    ('regular','Regular'),
    ('square','Square')
]


class Pizza(DynamicDocument):
    type = fields.StringField(max_length=20, choices=PIZZA_TYPE_CHOICE)
    size = fields.StringField(max_length=20)
    topping = fields.ListField(fields.StringField(max_length=40))

    def clean(self):
        for top in self.topping:
            pizzatopping = PizzaTopping.objects.filter(topping=top)
            if not pizzatopping :
                raise ValidationError({'topping':"{} topping is not present in database".format(top)})
        pizzasize = PizzaSize.objects.filter(size = self.size)
        if not pizzasize :
            raise ValidationError({'size':"{} size not present in database".format(self.size)})