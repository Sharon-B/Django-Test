from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# All blog posts view
def all_blog_posts(request):
    """
    A view to show the blog page
    """

    blog_posts = BlogPost.objects.all()

    template = 'blog/blog.html'

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, template, context)


# Blog detail view
def blog_detail(request, post_id):
    """
    A view to show individual blog post
    """
    post = get_object_or_404(BlogPost, pk=post_id)

    template = 'blog/blog_detail.html'

    context = {
        'post': post,
    }

    return render(request, template, context)
