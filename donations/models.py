from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    FOOD_TYPE_CHOICES = [
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
        ('snacks', 'Snacks'),
        ('fruits', 'Fruits'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('claimed', 'Claimed'),
        ('collected', 'Collected'),
        ('distributed', 'Distributed'),
        ('expired', 'Expired'),
    ]
    donor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='donations'
    )
    volunteer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='claimed_donations'
    )
    food_name = models.CharField(
        max_length=200
    )
    food_type = models.CharField(
        max_length=20,
        choices=FOOD_TYPE_CHOICES
    )
    quantity = models.PositiveIntegerField()

    pickup_location = models.CharField(
        max_length=300
    )
    available_until = models.DateTimeField()

    description = models.TextField(
        blank=True
    )
    urgency = models.IntegerField(
        default=1
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return f"{self.food_name} - {self.quantity}"