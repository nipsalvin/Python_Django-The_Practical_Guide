from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request=request, template_name='blog/index.html')

def all_posts(request):
    return render(request=request, template_name='blog/all_posts.html')

def post(request):
    pass