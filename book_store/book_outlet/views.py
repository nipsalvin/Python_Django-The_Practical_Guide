from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg, Sum

def index(request):
    books = Book.objects.all().order_by('title')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books':books,
        'total_books': num_books,
        'average_rating': avg_rating['rating__avg']})

def book_detail(request, slug):
    # # Method 1
    # book = get_object_or_404(Book, id)
    # return render(request, 'book_outlet/book_detail.html', {'book':book})
    # Method 2
    try:
        book = Book.objects.get(slug=slug)
        return render(request, 'book_outlet/book_detail.html', {'book':book})
    except:
        raise Http404()
    