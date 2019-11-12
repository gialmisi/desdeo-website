from django.shortcuts import render

from .models import Contents
from frontpage.views import subpages_list


def index(request):
    # singletons are always attributed the key 1
    try:
        content = Contents.objects.get(pk=1)
    except:
        content = None

    context = {
        "content": content,
        "subpages_list": subpages_list,
        "this_page": "about",
    }
    return render(request, "about/index.html", context)
