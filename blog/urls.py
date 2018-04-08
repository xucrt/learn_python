from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^post/', views.post, name='post'),
    #url(r'^post/(\d+)/', views.post, name='post'),
    #url(r'^post/(?P<post_id>\d+)/', views.post, name='post'),
    url(r'^detail/', views.detail, name='detail'),
]