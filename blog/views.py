from django.shortcuts import render
from .models import Post

def post_list(request):
    # Get all posts ordered by creation date
    posts = Post.objects.all().order_by('-created_date')
    # Render the template with the posts
    return render(request, 'blog/post_list.html', {'posts': posts})
