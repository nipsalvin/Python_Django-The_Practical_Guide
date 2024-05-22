from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Book(models.Model):
    title = models.CharField(max_length=50) 
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    author = models.CharField(max_length=50, null=True)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} - ({self.rating})"