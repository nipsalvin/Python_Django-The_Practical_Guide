from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateProfileView.as_view(), name='create_profile'),
    path('profiles_list/', views.ProfilesView.as_view(), name='profiles_list'),
] 