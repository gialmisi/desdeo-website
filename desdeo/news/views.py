from django.shortcuts import render

from .models import Article
from frontpage.views import subpages_list


def index(request):
    article_list = Article.objects.order_by("-pub_date").all()
    context = {
        "article_list": article_list,
        "subpages_list": subpages_list,
        "this_page": "news",
    }
    return render(request, "news/index.html", context)
