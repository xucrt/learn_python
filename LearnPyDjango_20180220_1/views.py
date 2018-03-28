
#下面的语句可以从官网里查到。老师的视频adv-6 1:05:10
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello world')