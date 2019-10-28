from django.shortcuts import render

from .models import BlogContent


def index(request):
    blog_list = BlogContent.objects.order_by("pub_date")

    # add a new attribute to the blog objects that contains the raw markdown strings
    for blog in blog_list:
        with blog.contents.open('r') as f:
            blog.contents_raw = "".join(f.readlines())

    context = {
        "blog_list": blog_list,
    }
    return render(request, "blog/index.html", context)
