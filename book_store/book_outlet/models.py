from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=50) 
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    author = models.CharField(max_length=50, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) #Slugify converts "Book Title" to "book-title"

    def __str__(self) -> str:
        return f"{self.title} - ({self.rating})"
    
    def get_absolute_url(self):
        """
        Returns the absolute URL for the book detail page by using reverse to call the function's name and pass the id as an argument

        :return: A string representing the absolute URL for the book detail page.

        :rtype: str
        """
        return reverse('book_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
