from django.shortcuts import render

from .models import BlogContent
from frontpage.views import subpages_list



def index(request):
    blog_list = BlogContent.objects.order_by("-pub_date").all()

    context = {
        "blog_list": blog_list,
        "subpages_list": subpages_list,
        "this_page": "blog",
    }
    return render(request, "blog/index.html", context)
