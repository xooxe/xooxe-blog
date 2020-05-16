from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.

def listPost(request):
    posts = Posts.objects.all().order_by('date')
    return render(request , 'posts/posts.html', {'posts':posts})

def postsDetails(request,slug):
    # return render(request , 'pages/about.html')
    # return HttpResponse(slug)
    post = Posts.objects.get(slug=slug)
    return render(request,'posts/detail.html' , {'post':post})