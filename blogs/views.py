from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, category
from django.db.models import Q

def posts_by_category(request, category_id):
    #Fetch the posts that belongs to the category with category_id
    posts = Blog.objects.filter(status='published', category = category_id)
    #Use try/expect when we want to do some custom action if the category does not exist
    #try:
     #   category = category.objects.get(pk=category_id)
    #except:
     #   #redirect the user to homepage
     #   return redirect('home')

    #use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(category, pk=category_id)

    context = {
        'posts' : posts,
        'category' : category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    
    context = {
        'blogs' : blogs,
        'keyword' : keyword,
    }

    return render(request, 'search.html', context)