from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, category

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
