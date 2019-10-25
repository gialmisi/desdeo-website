from django.shortcuts import render

from .models import Article


def index(request):
    article_list = Article.objects.all()
    context = {
        "article_list": article_list,
    }
    return render(request, "news/index.html", context)
