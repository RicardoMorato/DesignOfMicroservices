from django.db import models

from user.models import UserProfile


class Pizza(models.Model):
    PIZZA_TYPES = (
        ('MEET', 'Has Meet'),
        ('VEGGIE', 'Vegetarian'),
        ('VEGAN', 'Vegan')
    )
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    pizza_type = models.CharField(max_length=240, choices=PIZZA_TYPES, default=('MEET', 'Has Meet'))


class Pizzeria(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)


class Likes(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
