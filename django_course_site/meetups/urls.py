
from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', view=views.index, name='index'),
]