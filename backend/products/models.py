from django.db import models
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    CATEGORY_OPTIONS = (
        ("dairy","Dairy"),
        ("baverages","Baverages"),
        ("cereal", "Cereal"),
        ("personalcare","PersonalCare"),
        ("cleaningsupply", "CleaningSupply"),
        ("snacks","Snacks"),
        ("spicies", "Spicies")
    )
    name = models.CharField(max_length=225)
    barcode = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_OPTIONS)
    description = models.TextField(blank=True, null=True)
    price =  models.DecimalField(max_digits=10, decimal_places=2),
    stock_quantity =  models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name} ({self.barcode})"
