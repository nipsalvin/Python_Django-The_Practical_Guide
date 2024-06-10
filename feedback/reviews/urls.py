from django.urls import path
from . import views

urlpatterns = [
    # path('', views.review, name='index'),
    path('', views.ReviewView.as_view(), name='index'),
    # path('thank_you/', views.thank_you, name='thank_you'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews/', views.ReviewListView.as_view(), name='all_review'),
    path('reviews/<int:pk>/', views.SingleReviewView.as_view(), name='review_detail'),
]