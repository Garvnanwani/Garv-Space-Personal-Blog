from django.shortcuts import render, get_object_or_404
from operator import attrgetter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Email
from django.http import HttpResponse
# Create your views here.

def homepage(request):

    posts = {}

    blog_posts = sorted(Post.objects.all(),key = attrgetter('publish'), reverse = True)

    #Pagination

    page = request.GET.get('page', 1)

    paginator = Paginator(blog_posts, 3)

    
    if paginator.num_pages == 1:
        pass
    else:
        try:
            blog_posts = paginator.page(page)
        except PageNotAnInteger:
            blog_posts = paginator.page(1)
        except EmptyPage:
            blog_posts = paginator.page(paginator.num_pages)\

    if request.method == "POST":
        email = request.POST.get('email')
        
        email_add = Email(email = email)

        email_add.save()

    posts['blog_posts'] = blog_posts

    return render(request, 'index.html', posts)

def detail_blog_view(request, slug):
    
    context = {}

    blog_post = get_object_or_404(Post, slug=slug)

    context['blog_post'] = blog_post

    return render(request, 'content.html', context)