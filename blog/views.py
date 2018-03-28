from django.shortcuts import render
from django.http import HttpResponse
from blog import models

# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html!', {'blog_list':articles})

def detail(request):
    return HttpResponse('这是文章详情')