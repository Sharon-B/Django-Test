from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .models import BlogPost, BlogComment
from .forms import BlogCommentForm


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
    A view to show individual blog post,
    comments and leave a comment.
    """
    post = get_object_or_404(BlogPost, pk=post_id)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect(reverse('blog_detail', args=[post.id]))
        else:
            messages.error(request, 'Please check the form for errors. \
                Comment failed to post.')
    else:
        comment_form = BlogCommentForm()

    template = 'blog/blog_detail.html'

    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'new_comment': new_comment,
    }

    return render(request, template, context)
