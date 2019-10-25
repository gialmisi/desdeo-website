from django.shortcuts import render

from .models import BlogContent


def index(request):
    blog_list = BlogContent.objects.order_by("pub_date")

    blog_contents_list = []
    for blog in blog_list:
        with blog.contents.open('r') as f:
            blog_contents_list.append("".join(f.readlines()))

    context = {
        "blog_list": blog_list,
        "blog_contents_list": blog_contents_list,
    }
    return render(request, "blog/index.html", context)
