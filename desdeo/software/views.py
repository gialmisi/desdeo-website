from django.shortcuts import render

from .models import Content
from frontpage.views import subpages_list



def index(request):
    # singletons are always attributed the key 1
    try:
        content = Content.objects.get(pk=1)
    except:
        content = None

    print(content)

    context = {
        "content": content,
        "subpages_list": subpages_list,
        "this_page": "software",
    }

    return render(request, "software/index.html", context)
