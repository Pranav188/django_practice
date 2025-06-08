from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.CharField(("title"), max_length=50)
    rating = models.IntegerField(("rating"), validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(max_length=30, null=True)
    best_seller = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title} ({self.rating})"

# Create your models here.

