from django.shortcuts import render
from django.http import HttpResponse

from .models import Post,Comment




def index(request):
    #body
    return HttpResponse('<h1>welcome to django</h1>')

def home(request):
    return HttpResponse('<h1>welcom to our amlak</h1>')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'Post/post_list.html', context=context)

def post_detail(request, id):
    post = Post.objects.get(pk=id)
    comment = Comment.objects.filter(Post=post)
    context = {'post' : post,'comment' : comment}
    return render(request, 'Post/post_detail.html', context=context)

