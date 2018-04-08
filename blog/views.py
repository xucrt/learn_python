from django.shortcuts import render
from django.http import HttpResponse
from blog import models

# Create your views here.
def post_list(request):
    #print(request.META)
    return HttpResponse('This is a post list.')

def post(request):
    print(request.GET)
    pid = request.GET.get('id', '000')
    #print(pid)
    #return HttpResponse('This is a post %s' % post_id)
    #return HttpResponse('This is a post %s' % pid)
    #articles = models.Article.objects.all()
    #return render(request, 'blog/post.html')
    #return render(request, 'blog/post.html', {'id':pid})
    post = models.Post.objects.get(id=pid)
    return render(request, 'blog/post.html', {'post':post})

def detail(request):
    return HttpResponse('这是文章详情')