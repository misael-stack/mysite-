from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post
from django.utils import timezone
# blog/views.py

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blogapp/post_list.html', {'posts': posts})
