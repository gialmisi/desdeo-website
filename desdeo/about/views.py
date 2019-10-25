from django.shortcuts import render
from .models import AboutText


def index(request):
    # singletons are always attributed the key 1
    try:
        about_text = AboutText.objects.get(pk=1)
    except:
        about_text = None

    context = {
        "about_text": about_text,
    }
    return render(request, "about/index.html", context)
