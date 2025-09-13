from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("cashier", "Cashier")
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="cashier")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
            return f"{self.username} ({self.role})"