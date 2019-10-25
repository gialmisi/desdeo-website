from django.shortcuts import render

from .models import BibEntry


def index(request):
    bibentry_list = BibEntry.objects.order_by("year")[::-1]
    context = {
        "bibentry_list": bibentry_list,
    }
    return render(request, "publications/index.html", context)
