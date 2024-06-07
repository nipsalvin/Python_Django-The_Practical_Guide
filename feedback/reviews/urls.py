from django.urls import path
from . import views

urlpatterns = [
    # path('', views.review, name='index'),
    path('', views.ReviewView.as_view(), name='index'),
    path('thank_you/', views.thank_you, name='thank_you'),
]