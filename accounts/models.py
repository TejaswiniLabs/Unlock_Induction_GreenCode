from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('donor', 'Food Donor'),
        ('volunteer', 'Volunteer / NGO'),
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    phone = models.CharField(
        max_length=15
    )
    organization_name = models.CharField(
        max_length=150,
        blank=True
    )
    address = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f"{self.user.username} - {self.role}"