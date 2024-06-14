from django.urls import path
from blog.views import *


urlpatterns = [
    # path('', view=index, name='index'),
    path('', StartingPageView.as_view(), name='index'),
    # path('posts', view=all_posts, name='all_posts'),
    path('posts', AllPosts.as_view(), name='all_posts'),
    # path('posts/<slug:slug>', view=post_details, name='post_details'),
    path('posts/<slug:slug>', PostDetails.as_view(), name='post_details'),
]
