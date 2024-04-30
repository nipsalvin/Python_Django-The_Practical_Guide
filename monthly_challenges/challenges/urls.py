from django.urls import path
from . import views


urlpatterns = [
    # path('january/', views.january),
    # path('february/', view=views.february)
    # Adding int: infront of the month tells Django that the value required is an integer
    path('<int:month>/', view=views.monthly_challenge_by_number),
    # Adding str: infront of the month tells Django that the value required is a string
    path('<str:month>/', view=views.monthly_challenge, name='month-challenge')
]
