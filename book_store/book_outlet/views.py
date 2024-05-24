from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {'books':books})