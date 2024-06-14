from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from .forms import CommentForm

from .models import Post, Author, Tag

# def index(request):sst=request, template_name='blog/index.html', context=context)

class StartingPageView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.all().order_by('-date')[:3]
        context['posts'] = latest_posts
        return context


# def all_posts(request):
#     blog_posts = Post.objects.all().order_by('-date')
#     context = {'blog_posts':blog_posts}
#     return render(request=request, template_name='blog/all_posts.html', context=context)

class AllPosts(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'blog_posts'
    ordering = ['-date']


# def post_details(request, slug):    
#     """
#     Retrieves the post details based on the provided slug.
    
#     Parameters:
#         request (HttpRequest): The HTTP request object.
#         slug (str): The unique identifier of the post.
        
#     Returns:
#         HttpResponse: The rendered post details template with the context containing the identified post.
#     """
#     # blog_post = [post for post in blog_posts if post['slug'] == slug]
#     # identified_post = blog_post[0]
#     # context = {'post':identified_post}
#     identified_post = get_object_or_404(Post, slug=slug)
#     context = {'post':identified_post}
#     context['post_tags'] = identified_post.tags.all()
#     return render(request=request, template_name='blog/post_detail.html', context=context)

class PostDetails(View):
    template_name = 'blog/post_detail.html'
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm(),
            }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_details', args=[slug]))
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            }
        return render(request, self.template_name, context)