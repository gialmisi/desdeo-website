from django.shortcuts import render

from .models import FrameworkText


def index(request):
    # singletons are always attributed the key 1
    try:
        framework_text = FrameworkText.objects.get(pk=1)
    except:
        framework_text = None

    context = {
        "framework_text": framework_text,
    }    
    return render(request, "desdeoframework/index.html", context)
