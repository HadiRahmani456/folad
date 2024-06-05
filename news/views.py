from django.shortcuts import render, get_object_or_404

from .models import Post, Slid, Messenger_chat, Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import ListView


# Create your views here.


def posthome(request):
    posts = reversed(Post.objects.filter(status='published')[:8])
    slids = Slid.objects.filter(status='published')
    videos = reversed(Video.objects.filter(status='published')[:4])
    return render(request, 'post/home.html', {'posts': posts, 'slids' : slids, 'videos': videos})



# def postcategory(request):
#     posts = Post.objects.filter(status='published')
#     return render(request, 'post/categorypost.html', {'posts': posts})

class PostCategory(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'post/categorypost.html'

def videocategory(request):
    videos = Video.objects.filter(status='published')
    return render(request, 'post/categoryvideo.html', {'videos': videos})


def postsingle(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'post/single.html', {'posts': posts})



def relation(request):
    return render(request, 'post/relation.html')


def contactus(request):
    return render(request, 'post/contact.html')

def postdetail(request, post, pk):
    post = get_object_or_404(Post, slug=post, id=pk)
    return render(request, 'post/single.html', {'post': post})


def videodetail(request, post, pk):
    video = get_object_or_404(Video, slug=post, id=pk)
    return render(request, 'post/video_single.html', {'video': video})


def sliddetail(request, pk):
    slidd = get_object_or_404(Slid, id=pk)
    return render(request, 'post/sliddetaill.html', {'slidd': slidd})


def messenger(request):
    twi = Messenger_chat.objects.get(type='twitter')
    fac = Messenger_chat.objects.get(type='facebook')
    ins = Messenger_chat.objects.get(type='instagram')
    urls = {'twi': twi, 'fac': fac, 'ins': ins}
    return render(request, 'post/header.html', urls)
