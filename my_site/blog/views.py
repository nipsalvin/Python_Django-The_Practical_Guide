from datetime import date
from django.shortcuts import render
from .models import Post, Author, Tag

blog_posts = [

]


def get_date(post):
    return post.get('date')


def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    context = {'posts': latest_posts}
    return render(request=request, template_name='blog/index.html', context=context)


def all_posts(request):
    context = {'blog_posts':blog_posts}
    return render(request=request, template_name='blog/all_posts.html', context=context)


def post_details(request, slug):    
    """
    Retrieves the post details based on the provided slug.
    
    Parameters:
        request (HttpRequest): The HTTP request object.
        slug (str): The unique identifier of the post.
        
    Returns:
        HttpResponse: The rendered post details template with the context containing the identified post.
    """
    # blog_post = [post for post in blog_posts if post['slug'] == slug]
    # identified_post = blog_post[0]
    # context = {'post':identified_post}
    identified_post = next(post for post in blog_posts if post['slug'] == slug)
    context = {'post':identified_post}
    return render(request=request, template_name='blog/post_detail.html', context=context)
