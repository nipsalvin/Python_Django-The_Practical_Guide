from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    # path('<int:id>', views.book_detail, name='book_detail'),
    path('<slug:slug>', views.book_detail, name='book_detail'),
]