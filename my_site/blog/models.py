from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True ,null=False, db_index=True, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(3000)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)