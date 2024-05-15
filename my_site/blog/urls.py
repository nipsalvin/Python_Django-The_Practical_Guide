from django.urls import path
from blog.views import *


urlpatterns = [
    path('', view=index, name='index'),
    path('posts', view=all_posts, name='all_posts'),
    path('posts/<slug>', view=post_details, name='post_details'),
]
