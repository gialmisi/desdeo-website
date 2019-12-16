from django.shortcuts import render

from .models import Content, Downloadable
from frontpage.views import subpages_list


def index(request):
    # singletons are always attributed the key 1
    try:
        content = Content.objects.get(pk=1)
    except:
        content = None

    downloadables_list = Downloadable.objects.all()

    context = {
        "content": content,
        "downloadables_list": downloadables_list,
        "subpages_list": subpages_list,
        "this_page": "about",
    }
    return render(request, "about/index.html", context)
