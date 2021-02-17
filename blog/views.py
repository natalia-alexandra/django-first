from django.shortcuts import get_object_or_404, render
from .models import Blog

# Create your views here.


def blog(req):
    blog = Blog.objects
    return render(req, 'blog/blog.html', {'blog': blog})


def article(req, article_id):
    article = get_object_or_404(Blog, pk=article_id)
    return render(req, 'blog/article.html', {'article': article})
