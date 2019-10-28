from django.shortcuts import render

from .models import SoftwareText


def index(request):
    # singletons are always attributed the key 1
    try:
        software_text = SoftwareText.objects.get(pk=1)
    except:
        software_text = None

    context = {
        "software_text": software_text,
    }

    return render(request, "software/index.html", context)
