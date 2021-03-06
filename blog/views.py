from django.shortcuts import render, redirect
from .forms import NewBlogPost
from .models import Blog
from django.urls import reverse
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.


def view_blogs(request):
    """ Homepage with blog  also shows the 4 latest objects in a sidebar """
    blogs = Blog.objects.all()
    products = Product.objects.all().order_by('-id')[:4]
    context = {
        'blogs': blogs,
        'products': products
    }
    return render(request, 'blog/blog.html', context)


@login_required
def add_blog(request):
    if request.user.is_superuser:
        if request.method == 'GET':

            form = NewBlogPost
            context = {
                'form': form
            }
            return render(request, 'blog/add_blog.html', context)
        elif request.method == 'POST':
            form = NewBlogPost(request.POST)
            if form.is_valid():
                new_blog = form.save()

    return redirect(reverse(view_blogs))

@login_required
def edit_blog(request, blog_id):
    if request.user.is_superuser:
        if request.method == 'GET':
            blog = Blog.objects.get(pk=blog_id)
            form = NewBlogPost(instance=blog)
            context = {
                    'form': form,
                    'blog': blog
                }
            return render(request, 'blog/edit_blog.html', context)
        elif request.method == 'POST':
            instance = Blog.objects.get(pk=blog_id)
            form = NewBlogPost(request.POST, instance=instance)
            if form.is_valid():
                new_blog = form.save()

    return redirect(reverse(view_blogs))



@login_required
def delete_blog(request, blog_id):
    if request.user.is_superuser:
        blog = Blog.objects.get(pk=blog_id)
        blog.delete()
    return redirect(reverse(view_blogs))
    