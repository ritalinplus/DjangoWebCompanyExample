from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

def category(request, category_id):
    category_obj = get_object_or_404(Category, id=category_id)
    print(category_obj)
    return render(request, "blog/category.html", {'category': category_obj})
