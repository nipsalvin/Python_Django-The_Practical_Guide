from django.urls import path
from . import views


urlpatterns = [
    # path('january/', views.january),
    # path('february/', view=views.february)
    path('<month>/', view=views.monthly_challenges)
]

