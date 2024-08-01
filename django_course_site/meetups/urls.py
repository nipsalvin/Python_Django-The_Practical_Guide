
from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', view=views.index, name='index'),
    path('meetups/success', view=views.confirm_registration, name='confirm_registration'),
    path('meetups/<slug:meetup_slug>', view=views.meetup_details, name='meetup_details'),
]