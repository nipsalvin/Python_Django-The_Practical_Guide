
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<slug:meetup_slug>/success', view=views.confirm_registration, name='confirm_registration'),
    path('<slug:meetup_slug>', view=views.meetup_details, name='meetup_details'),
]